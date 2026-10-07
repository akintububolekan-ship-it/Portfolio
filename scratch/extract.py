import re

with open(r"C:\Users\HP\.gemini\antigravity\brain\7a5e906f-81a6-45aa-836b-28f86646166b\.system_generated\steps\53\output.txt", "r", encoding="utf-8") as f:
    data = f.read()

texts = re.findall(r'<text [^>]*name="([^"]+)"', data)

unique_texts = []
for t in texts:
    if len(t) > 20 and t not in unique_texts:
        unique_texts.append(t)

for t in unique_texts:
    print(t)
