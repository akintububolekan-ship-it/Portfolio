import re

with open(r"C:\Users\HP\.gemini\antigravity\brain\7a5e906f-81a6-45aa-836b-28f86646166b\.system_generated\steps\53\output.txt", "r", encoding="utf-8") as f:
    data = f.read()

texts = re.findall(r'<text [^>]*name="([^"]+)"', data)

with open(r"C:\Users\HP\Downloads\Portfolio\scratch\full_texts.txt", "w", encoding="utf-8") as out:
    for t in texts:
        out.write(t + "\n")
