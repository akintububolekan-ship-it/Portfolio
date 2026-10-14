with open(r'C:/Users/HP/.gemini/antigravity/brain/7553566c-0120-4577-b87d-1966a417eed5/.system_generated/steps/986/output.txt', encoding='utf-8') as f:
    text = f.read()

import re

for line in text.splitlines():
    if '<text' in line:
        name_match = re.search(r'name="([^"]+)"', line)
        if name_match:
            name = name_match.group(1).strip()
            if name in ['Features', 'Tools']:
                print(line)
