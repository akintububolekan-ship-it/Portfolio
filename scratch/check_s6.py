import xml.etree.ElementTree as ET

with open(r'C:/Users/HP/.gemini/antigravity/brain/73bef1fa-b7ab-4dc9-b138-9fa87b4d2598/.system_generated/steps/21/output.txt', 'r', encoding='utf-8') as f:
    xml_content = ''.join([l for l in f if not l.startswith('IMPORTANT:')])

root = ET.fromstring(xml_content)
f6 = root.find('.//*[@id="508:12096"]')
print("f6:", f6.attrib)
for c in f6.iter():
    print(c.tag, c.attrib)

# check if there is an image between f6 and next section
main_frame = root.find('.//*[@id="487:11993"]')
children = list(main_frame)
idx6 = children.index(f6)
print("Section 6 index:", idx6, "of", len(children))
for i in range(idx6, len(children)):
    print(i, children[i].tag, children[i].attrib.get('id'), children[i].attrib.get('name'))
