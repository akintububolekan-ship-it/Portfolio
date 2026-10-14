with open(r'C:\Users\HP\.gemini\antigravity\brain\a5743cf2-2c8b-4925-9d8a-233014efb3cf\.system_generated\steps\15\output.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re

idx = text.find('name="Frame 1000005430"')
chunk = text[idx:idx+150000]

# find direct frame tags with indentation 11 spaces or x, y coordinates
frames = re.findall(r'<frame id="([^"]+)" name="([^"]+)" x="([^"]+)" y="([^"]+)" width="([^"]+)" height="([^"]+)"', chunk)

# Group frames by level or find big ones
for fr in frames:
    w = float(fr[4])
    h = float(fr[5])
    if w >= 200:
        print(fr)
