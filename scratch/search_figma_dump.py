with open(r'C:/Users/HP/.gemini/antigravity/brain/7553566c-0120-4577-b87d-1966a417eed5/.system_generated/steps/967/output.txt', encoding='utf-8') as f:
    text = f.read()

import re
root_match = re.search(r'<(\w+)[^>]+id="([^"]+)"[^>]+name="([^"]+)"', text)
print("Root:", root_match.groups() if root_match else "None")

children = re.findall(r'<frame[^>]+id="([^"]+)"[^>]+name="([^"]+)"', text)
print(f"Total frame nodes: {len(children)}")
for cid, cname in children[:25]:
    print(cid, "->", cname)
