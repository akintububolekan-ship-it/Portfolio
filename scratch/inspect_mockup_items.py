import xml.etree.ElementTree as ET

with open(r'C:\Users\HP\.gemini\antigravity\brain\7a5e906f-81a6-45aa-836b-28f86646166b\.system_generated\steps\53\output.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

root = ET.fromstring(''.join(lines[:-1]))

container = root.find('.//frame[@id="432:21649"]')
print("Container 432:21649:")
for c in container:
    print("---", c.attrib.get('id'), c.attrib.get('name'), "y=", c.attrib.get('y'))
    # look for labels and sub-frames
    for sub in c:
        print("   sub:", sub.attrib.get('id'), sub.attrib.get('name'), "y=", sub.attrib.get('y'))
        for subsub in sub:
            print("      subsub:", subsub.attrib.get('id'), subsub.attrib.get('name'))
