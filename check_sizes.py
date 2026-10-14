import os
import re

out_path = r'C:\Users\HP\.gemini\antigravity\brain\a5743cf2-2c8b-4925-9d8a-233014efb3cf\.system_generated\steps\15\output.txt'

lines = open(out_path, 'r', encoding='utf-8').read().split('\n')

elements = []
for line in lines:
    m = re.search(r'name="(Frame 1000005[0-9]+|Video Project 9[^"]*)"\s+x="([^"]+)"\s+y="([^"]+)"\s+width="([^"]+)"\s+height="([^"]+)"', line)
    if m:
        name = m.group(1)
        x = float(m.group(2))
        y = float(m.group(3))
        w = float(m.group(4))
        h = float(m.group(5))
        elements.append((name, x, y, w, h))

# Remove duplicates (some frames might be nested inside same-named frames)
unique = {}
for e in elements:
    # use name as key if we only care about unique names
    unique[e[0]] = e
    
sorted_elements = sorted(unique.values(), key=lambda e: (round(e[2]/10)*10, e[1])) # sort by roughly y, then x

for e in sorted_elements:
    print(e)
