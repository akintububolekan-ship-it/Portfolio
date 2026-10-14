import glob

files = sorted(glob.glob('*.html'))
for f in files:
    content = open(f, encoding='utf-8').read()
    if '        <link rel="icon"' in content:
        content = content.replace('        <link rel="icon"', '    <link rel="icon"')
        open(f, 'w', encoding='utf-8').write(content)
print('Indentation standardized')
