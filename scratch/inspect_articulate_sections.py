import xml.etree.ElementTree as ET

with open(r'C:/Users/HP/.gemini/antigravity/brain/73bef1fa-b7ab-4dc9-b138-9fa87b4d2598/.system_generated/steps/21/output.txt', 'r', encoding='utf-8') as f:
    xml_content = ''.join([l for l in f if not l.startswith('IMPORTANT:')])

root = ET.fromstring(xml_content)

# Find Frame 1000005340 (id 487:11993)
main_frame = root.find('.//*[@id="487:11993"]')
print("Found main_frame:", main_frame.attrib)

for idx, child in enumerate(main_frame):
    print(f"\n--- Section {idx}: <{child.tag} id='{child.attrib.get('id')}' name='{child.attrib.get('name')}' y='{child.attrib.get('y')}' h='{child.attrib.get('height')}'> ---")
    # print direct children of this section
    for sub in child:
        print(f"    <{sub.tag} id='{sub.attrib.get('id')}' name='{sub.attrib.get('name')}' y='{sub.attrib.get('y')}' h='{sub.attrib.get('height')}'>")
