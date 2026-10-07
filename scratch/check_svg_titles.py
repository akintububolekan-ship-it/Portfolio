import glob
import re

svgs = glob.glob('images/Articulate Images/UI/*.svg')
for s in sorted(svgs):
    with open(s, 'r', encoding='utf-8') as f:
        c = f.read()
    # Find text or title in SVG
    texts = re.findall(r'>([^<]{3,35})<', c)
    # Filter out common CSS/tag stuff
    meaningful = [t.strip() for t in texts if not t.strip().startswith(('http', 'M', 'd', 'url', 'clip', 'fill', 'stroke')) and len(t.strip()) > 3]
    print(f"{s:45} | First texts: {meaningful[:5]}")
