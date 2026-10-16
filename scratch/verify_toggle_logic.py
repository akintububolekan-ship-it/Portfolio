import glob, re

files = sorted(glob.glob('*.html'))
for f in files:
    content = open(f, encoding='utf-8').read()
    if 'function toggleSection' in content:
        # find the full function
        m = re.search(r'function toggleSection\(id, btn\)\s*\{[\s\S]*?\}', content)
        if m:
            func = m.group(0)
            if 'Close' not in func or 'View' not in func:
                print(f"ANOMALY in {f}:")
                print(func)
            else:
                # check if 'Close' is set when opening and 'View' when closing
                lines = [l.strip() for l in func.split('\n')]
                # print summary
                # print(f"{f}: OK")
print("Check complete")
