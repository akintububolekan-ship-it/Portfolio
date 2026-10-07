import os
import glob
import re

svg_files = glob.glob(r'images/Articulate Images/UI/*.svg')

for f in sorted(svg_files):
    name = os.path.basename(f)
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read(1000)
    # find viewBox and clip0
    vb = re.search(r'viewBox="([^"]+)"', content)
    clip = re.search(r'clip0_([0-9_]+)', content)
    vb_str = vb.group(1) if vb else ''
    clip_str = clip.group(1).replace('_', ':') if clip else ''
    print(f"{name:25} | viewBox: {vb_str:20} | clip-node: {clip_str}")
