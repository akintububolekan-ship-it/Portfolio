import xml.etree.ElementTree as ET

with open(r'C:\Users\HP\.gemini\antigravity\brain\7a5e906f-81a6-45aa-836b-28f86646166b\.system_generated\steps\53\output.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

root = ET.fromstring(''.join(lines[:-1]))

container = root.find('.//frame[@id="432:20920"]')
for c in container:
    print(c.tag, c.attrib.get('id'), c.attrib.get('name'), 'y=', c.attrib.get('y'))

print('--- Children of 432:20931 ---')
f_main = container.find('.//frame[@id="432:20931"]')
for c in f_main:
    print(c.tag, c.attrib.get('id'), c.attrib.get('name'), 'y=', c.attrib.get('y'))
