import glob, re

files = sorted(glob.glob('*.html'))
non_close = []
for f in files:
    content = open(f, encoding='utf-8').read()
    matches = re.findall(r'<button[^>]*class=[\"\']section-header__action[\"\'][^>]*>(.*?)</button>', content, re.DOTALL)
    for m in matches:
        text = m.strip()
        if text != 'Close':
            non_close.append((f, text))

print(f"Total non-Close buttons: {len(non_close)}")
for item in non_close:
    print(item)
