import re
import os

svg_files = [
    'Dashboard.svg',
    'Frame 1000005226.svg',
    'Frame 1000005340.svg',
    'Frame 1000005343.svg',
    'Frame 564.svg',
    'Other screens 3.svg',
    'Other screens 4.svg',
    'Other screens 4-1.svg',
    'Other screens 4-2.svg',
    'Other screens 4-3.svg',
    'Other screens 4-4.svg',
    'Other screens 5.svg',
    'Other screens 6.svg',
    'Other screens 7.svg',
    'Other screens 8.svg',
    'Other screens 9.svg',
    'Other screens 10.svg',
    'Other screens 11.svg',
    'Other screens 12.svg',
    'Other screens 13.svg',
    'Other screens 14.svg',
    'Call management.svg',
]

for fname in svg_files:
    path = os.path.join(r'c:\Users\HP\Downloads\Portfolio\images\UI', fname)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        texts = re.findall(r'>([^<]{3,60})<', content)
        clean_texts = [t.strip() for t in texts if t.strip() and not t.strip().startswith('var') and not t.strip().startswith('{')][:6]
        print(f"{fname:24} -> {clean_texts}")
    else:
        print(f"{fname:24} -> NOT FOUND")
