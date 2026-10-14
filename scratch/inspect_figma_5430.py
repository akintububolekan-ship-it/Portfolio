with open(r'C:\Users\HP\.gemini\antigravity\brain\a5743cf2-2c8b-4925-9d8a-233014efb3cf\.system_generated\steps\15\output.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find Frame 1000005430
idx = text.find('name="Frame 1000005430"')
print("Found Frame 1000005430 at", idx)

# Inspect frames inside Frame 1000005430
chunk = text[idx:idx+8000]
frames = re.findall(r'<frame id="([^"]+)" name="([^"]+)" x="([^"]+)" y="([^"]+)" width="([^"]+)" height="([^"]+)"', chunk)
print(f"Total frames found: {len(frames)}")
for fr in frames:
    print(fr)
