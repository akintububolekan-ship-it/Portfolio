import glob

fav_tags = '''    <link rel="icon" type="image/png" href="images/Profile image.png" />
    <link rel="icon" type="image/x-icon" href="favicon.ico" />
    <link rel="apple-touch-icon" href="images/Profile image.png" />
'''

files = sorted(glob.glob('*.html'))
updated = []
for f in files:
    if f.startswith('test_') or f == 'index.html':
        continue
    content = open(f, encoding='utf-8').read()
    if 'rel="icon"' in content or "rel='icon'" in content:
        continue
    if '<link rel="stylesheet"' in content:
        new_content = content.replace('<link rel="stylesheet"', fav_tags + '    <link rel="stylesheet"', 1)
    elif '</head>' in content:
        new_content = content.replace('</head>', fav_tags + '</head>', 1)
    else:
        continue
    with open(f, 'w', encoding='utf-8') as out:
        out.write(new_content)
    updated.append(f)

print(f"Updated {len(updated)} files: {updated}")
