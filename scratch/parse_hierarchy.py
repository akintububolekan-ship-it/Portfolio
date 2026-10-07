import re

with open(r'C:\Users\HP\.gemini\antigravity\brain\7a5e906f-81a6-45aa-836b-28f86646166b\.system_generated\steps\53\output.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's write a parser that parses the xml hierarchy properly and sorts frames by y position
# or just prints the frames with their bounding boxes (x, y, width, height) and all direct/nested text.

# Since output.txt is well-structured xml-like:
lines = text.splitlines()

current_frame = None
frames = []

for line in lines:
    m = re.search(r'<frame id="([^"]+)" name="([^"]+)" x="([^"]+)" y="([^"]+)" width="([^"]+)" height="([^"]+)"', line)
    if m:
        fid, fname, x, y, w, h = m.groups()
        frames.append({
            'id': fid,
            'name': fname,
            'x': float(x),
            'y': float(y),
            'w': float(w),
            'h': float(h),
            'line': line
        })

print(f"Total frames: {len(frames)}")

# Let's inspect the children of 432:20920 and 432:20931
