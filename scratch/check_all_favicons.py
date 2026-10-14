import glob

files = sorted(glob.glob('*.html'))
for f in files:
    if f.startswith('test_'):
        continue
    content = open(f, encoding='utf-8').read()
    has_fav = 'rel="icon"' in content or "rel='icon'" in content
    print(f"{f}: has_favicon={has_fav}")
