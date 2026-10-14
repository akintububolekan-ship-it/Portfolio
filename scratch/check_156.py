with open('images/Haystack shorts/Frame 1000005432.svg', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = [m for m in re.finditer(r'156', text)]
print(f"Occurrences of 156: {len(matches)}")
for m in matches[:5]:
    start = max(0, m.start() - 50)
    end = min(len(text), m.end() + 50)
    print(text[start:end])
