with open('images/Haystack shorts/Frame 1000005432.svg', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# check any rect or line with y=0 or y<=1
matches = re.findall(r'<[^>]+y=\"[01]\.?[0-9]*\"[^>]*>', text)
for m in matches[:10]:
    print(m[:120])
