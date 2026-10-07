import xml.etree.ElementTree as ET

with open(r'C:/Users/HP/.gemini/antigravity/brain/73bef1fa-b7ab-4dc9-b138-9fa87b4d2598/.system_generated/steps/21/output.txt', 'r', encoding='utf-8') as f:
    xml_content = ''.join([l for l in f if not l.startswith('IMPORTANT:')])

root = ET.fromstring(xml_content)

f_7 = root.find('.//*[@id="508:12101"]')
print("Section 7 attributes:", f_7.attrib)

for child in f_7:
    print(f"Child: <{child.tag} id='{child.attrib.get('id')}' name='{child.attrib.get('name')}' y='{child.attrib.get('y')}' h='{child.attrib.get('height')}'> (len={len(child)})")
    if child.attrib.get('id') == '508:12110':
        for sub in child:
            print(f"  Sub: <{sub.tag} id='{sub.attrib.get('id')}' name='{sub.attrib.get('name')}' y='{sub.attrib.get('y')}' h='{sub.attrib.get('height')}'> (len={len(sub)})")
            for sub2 in sub:
                print(f"    Sub2: <{sub2.tag} id='{sub2.attrib.get('id')}' name='{sub2.attrib.get('name')}' y='{sub2.attrib.get('y')}' h='{sub2.attrib.get('height')}'> (len={len(sub2)})")
