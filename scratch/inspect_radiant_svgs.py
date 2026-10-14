import re
import os

folder = r"c:\Users\HP\Downloads\Portfolio\images\Radiant glow"
for f in os.listdir(folder):
    if not f.endswith(".svg"):
        continue
    path = os.path.join(folder, f)
    with open(path, "r", encoding="utf-8", errors="ignore") as fp:
        head = fp.read(2000)
    svg_match = re.search(r'<svg([^>]+)>', head)
    if svg_match:
        attrs = svg_match.group(1)
        w = re.search(r'width="([^"]+)"', attrs)
        h = re.search(r'height="([^"]+)"', attrs)
        vb = re.search(r'viewBox="([^"]+)"', attrs)
        print(f"{f}: width={w.group(1) if w else None}, height={h.group(1) if h else None}, viewBox={vb.group(1) if vb else None}")
        filters = re.findall(r'<([a-zA-Z0-9]+)[^>]*filter="url\(#([^"]+)\)"', head)
        if filters:
            print(f"  filters: {filters}")
        rect_bg = re.search(r'<rect width="([^"]+)" height="([^"]+)" transform="translate\(([^"]+)\)" fill="white"', head)
        if rect_bg:
            print(f"  Inner rect bg: width={rect_bg.group(1)}, height={rect_bg.group(2)}, translate={rect_bg.group(3)}")
