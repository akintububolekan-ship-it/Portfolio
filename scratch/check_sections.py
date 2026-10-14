with open(r'C:\Users\HP\.gemini\antigravity\brain\a5743cf2-2c8b-4925-9d8a-233014efb3cf\.system_generated\steps\15\output.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'<frame id="([^"]+)" name="([^"]+)" x="([^"]+)" y="([^"]+)" width="([^"]+)" height="([^"]+)"', text)
for m in matches:
    try:
        w = float(m[4])
        h = float(m[5])
        y = float(m[3])
        if 630 <= w <= 650:
            print(f"{m[1]} (id={m[0]}): y={y}, w={w}, h={h}")
    except:
        pass
