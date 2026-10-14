import re
import os

folder = r"c:\Users\HP\Downloads\Portfolio\images\Baze air"
files = ["Frame 86.svg", "Frame 1000005226.svg", "Frame 1000005227.svg", "Container.svg", "Container-1.svg"]

for f in files:
    path = os.path.join(folder, f)
    if not os.path.exists(path):
        print(f"Missing: {f}")
        continue
    with open(path, "r", encoding="utf-8", errors="ignore") as fp:
        head = fp.read(2000)
    svg_match = re.search(r'<svg([^>]+)>', head)
    if svg_match:
        attrs = svg_match.group(1)
        w = re.search(r'width="([^"]+)"', attrs)
        h = re.search(r'height="([^"]+)"', attrs)
        vb = re.search(r'viewBox="([^"]+)"', attrs)
        print(f"{f}: width={w.group(1) if w else None}, height={h.group(1) if h else None}, viewBox={vb.group(1) if vb else None}")
        # Check first child elements
        first_tags = re.findall(r'<([a-zA-Z0-9]+)[^>]*filter="url\(#([^"]+)\)"', head)
        if first_tags:
            print(f"  Has filter element: {first_tags}")
        rect_bg = re.search(r'<rect width="([^"]+)" height="([^"]+)" transform="translate\(([^"]+)\)" fill="white"', head)
        if rect_bg:
            print(f"  Inner rect bg: width={rect_bg.group(1)}, height={rect_bg.group(2)}, translate={rect_bg.group(3)}")
        else:
            rect_bg2 = re.search(r'<rect width="([^"]+)" height="([^"]+)" fill="white"', head)
            if rect_bg2:
                print(f"  Inner rect bg (no translate): width={rect_bg2.group(1)}, height={rect_bg2.group(2)}")
