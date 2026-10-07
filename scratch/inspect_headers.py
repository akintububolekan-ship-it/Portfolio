import xml.etree.ElementTree as ET

with open(r'C:\Users\HP\.gemini\antigravity\brain\7a5e906f-81a6-45aa-836b-28f86646166b\.system_generated\steps\53\output.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

root = ET.fromstring(''.join(lines[:-1]))

# Find all frames with section titles or buttons
for frame in root.findall('.//frame'):
    # check if frame has a button or section title
    texts = [t.attrib.get('name') for t in frame.findall('.//text')]
    if any(k in ' '.join(texts) for k in ['Design Process', 'Problem', 'Goal', 'Research', 'Methodology', 'Competitor', 'Insights', 'Solution']):
        print(f"[{frame.attrib.get('id')}] y={frame.attrib.get('y')} texts={texts[:5]}")
