with open(r'C:\Users\HP\.gemini\antigravity\brain\a5743cf2-2c8b-4925-9d8a-233014efb3cf\.system_generated\steps\15\output.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re

for fid in ['736:16864', '737:21809', '737:20201']:
    idx = text.find(f'id="{fid}"')
    if idx != -1:
        print(text[idx:idx+300])
