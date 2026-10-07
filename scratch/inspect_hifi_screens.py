import xml.etree.ElementTree as ET

with open(r'C:/Users/HP/.gemini/antigravity/brain/73bef1fa-b7ab-4dc9-b138-9fa87b4d2598/.system_generated/steps/21/output.txt', 'r', encoding='utf-8') as f:
    xml_content = ''.join([l for l in f if not l.startswith('IMPORTANT:')])

root = ET.fromstring(xml_content)

for nid in ['520:14207', '520:14055', '508:13359', '508:12838', '508:15237']:
    node = root.find(f'.//*[@id="{nid}"]')
    if node is not None:
        print(f"\n==================== NODE {nid}: {node.attrib.get('name')} ====================")
        for child in node:
            print(f"  <{child.tag} id='{child.attrib.get('id')}' name='{child.attrib.get('name')}' y='{child.attrib.get('y')}' h='{child.attrib.get('height')}'>")
            for sub in child:
                print(f"    <{sub.tag} id='{sub.attrib.get('id')}' name='{sub.attrib.get('name')}' y='{sub.attrib.get('y')}' h='{sub.attrib.get('height')}'>")
