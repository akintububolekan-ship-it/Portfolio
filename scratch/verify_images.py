import re
import os

with open(r'c:\Users\HP\Downloads\Portfolio\rihub.html', 'r', encoding='utf-8') as f:
    html = f.read()

images = re.findall(r'<img[^>]+src="([^">]+)"', html)

print(f"Total image tags: {len(images)}")
missing = []
for img in images:
    path = os.path.join(r'c:\Users\HP\Downloads\Portfolio', img.replace('/', os.sep))
    if not os.path.exists(path):
        missing.append(img)
    else:
        print(f"OK: {img}")

if missing:
    print("MISSING:", missing)
else:
    print("All image files exist!")
