import glob, re

files = sorted(glob.glob('*.html'))
found = []
for f in files:
    content = open(f, encoding='utf-8').read()
    buttons = re.findall(r'<button[^>]*class=[\"\']section-header__action[\"\'][^>]*>(.*?)</button>', content, re.DOTALL)
    for b in buttons:
        if 'View' in b or 'view' in b:
            found.append((f, b.strip()))

print(f"Total 'View' buttons found: {len(found)}")
for item in found:
    print(item)
