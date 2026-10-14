with open('images/Haystack shorts/Frame 1000005432.svg', 'r', encoding='utf-8') as f:
    text = f.read()

import re
lines = re.findall(r'<line[^>]+>|<rect[^>]+>|<path[^>]+stroke[^>]+>', text)
print(f"Total stroke/rect elements in Frame 1000005432: {len(lines)}")
for l in lines[:10]:
    print(" ", l[:100])
