import xml.etree.ElementTree as ET

with open(r'C:\Users\HP\.gemini\antigravity\brain\7a5e906f-81a6-45aa-836b-28f86646166b\.system_generated\steps\53\output.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

root = ET.fromstring(''.join(lines[:-1]))

final_design = root.find('.//frame[@id="432:21636"]')
print("Final design tag:", final_design.attrib)

for c in final_design:
    print("  Child:", c.attrib.get('id'), c.attrib.get('name'), "y=", c.attrib.get('y'))
    # find any subframes with labels or mockups
    for sub in c:
        print("    Sub:", sub.attrib.get('id'), sub.attrib.get('name'), "y=", sub.attrib.get('y'))
        for subsub in sub:
            print("      SubSub:", subsub.attrib.get('id'), subsub.attrib.get('name'), "y=", subsub.attrib.get('y'))
