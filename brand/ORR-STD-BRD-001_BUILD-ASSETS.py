#!/usr/bin/env python3
"""Generate/check ORR-STD-BRD-001 r03 brand renditions; Python standard library only."""
import argparse
import csv
import io
import json
from pathlib import Path
import re

BASE = Path(__file__).resolve().parent
ID = "ORR-STD-BRD-001"

def kebab(value):
    return re.sub(r"(?<!^)(?=[A-Z])", "-", value).lower()

def luminance(value):
    rgb = [int(value[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    rgb = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in rgb]
    return sum(v * w for v, w in zip(rgb, (0.2126, 0.7152, 0.0722)))

def ratio(fg, bg):
    a, b = sorted((luminance(fg), luminance(bg)))
    return (b + 0.05) / (a + 0.05)

def csv_text(headers, rows):
    out = io.StringIO(newline="")
    writer = csv.writer(out, lineterminator="\n")
    writer.writerow(headers)
    writer.writerows(rows)
    return out.getvalue()

def render(data):
    assert data['documentId'] == ID and data['status'] == 'Draft'
    colors = data['colors']
    assert all(re.fullmatch(r'#[0-9A-F]{6}', value) for value in colors.values())
    assert all(key in colors for key in data['semantic'].values())
    lines = [f"/* {ID} {data['revision']} — Draft; generated from TOKENS.json. */", ":root {"]
    lines += [f"  --orr-color-{kebab(key)}: {value};" for key, value in colors.items()]
    lines += [f"  --orr-{kebab(key)}: var(--orr-color-{kebab(value)});" for key, value in data['semantic'].items()]
    for key, value in data['typography'].items():
        suffix = 'rem' if key.endswith('Rem') else ''
        lines.append(f"  --orr-type-{kebab(key)}: {value}{suffix};")
    lines += [f"  --orr-space-{i}: {value}px;" for i, value in enumerate(data['spacingPx'], 1)]
    lines += [f"  --orr-{kebab(key)}: {value}px;" for key, value in data['geometry'].items()]
    lines += [f"  --orr-duration: {data['motion']['durationMs']}ms;", f"  --orr-easing: {data['motion']['easing']};", "}", "@media (prefers-reduced-motion: reduce) {", f"  :root {{ --orr-duration: {data['motion']['reducedMotionDurationMs']}ms; }}", "}", ""]
    checks = []
    for pair in data['contrastPairs']:
        value = ratio(colors[pair['foreground']], colors[pair['background']])
        checks.append({**pair, 'ratio': value, 'result': 'PASS' if value >= pair['minimum'] else 'FAIL'})
    outputs = {
        f'{ID}_TOKENS.css': '\n'.join(lines),
        f'{ID}_PALETTE.csv': csv_text(['document_id', 'revision', 'token', 'hex', 'red', 'green', 'blue'],
            [[ID, data['revision'], key, value, *[int(value[i:i+2], 16) for i in (1, 3, 5)]] for key, value in colors.items()]),
        f'{ID}_CONTRAST.csv': csv_text(['document_id', 'revision', 'pair', 'foreground', 'background', 'ratio_display', 'minimum', 'result'],
            [[ID, data['revision'], c['name'], colors[c['foreground']], colors[c['background']], f"{c['ratio']:.4f}", c['minimum'], c['result']] for c in checks])
    }
    return outputs, checks

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--write', action='store_true')
    mode.add_argument('--check', action='store_true')
    args = parser.parse_args()
    data = json.loads((BASE / f'{ID}_TOKENS.json').read_text())
    outputs, checks = render(data)
    mismatches = []
    for name, contents in outputs.items():
        path = BASE / name
        if args.write:
            path.write_text(contents, encoding='utf-8')
        elif not path.exists() or path.read_text() != contents:
            mismatches.append(name)
    failed = [c for c in checks if c['result'] == 'FAIL']
    print(json.dumps({'document_id': ID, 'revision': data['revision'], 'mode': 'write' if args.write else 'check',
        'generated_files': list(outputs), 'mismatches': mismatches, 'contrast_pairs': len(checks),
        'failed_pairs': failed, 'result': 'PASS' if not failed and not mismatches else 'FAIL',
        'limits': 'Declared sRGB pairs only, full precision thresholds; not full rendered accessibility or release approval.'}, indent=2))
    return 1 if failed or mismatches else 0

if __name__ == '__main__':
    raise SystemExit(main())
