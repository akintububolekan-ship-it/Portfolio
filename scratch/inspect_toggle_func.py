import glob, re

files = sorted(glob.glob('*.html'))
for f in files:
    content = open(f, encoding='utf-8').read()
    if 'function toggleSection' in content:
        match = re.search(r'function toggleSection\(.*?\)\s*\{.*?\}', content, re.DOTALL)
        if match:
            print(f"=== {f} ===")
            print(match.group(0))
