import xml.etree.ElementTree as ET

with open(r'C:/Users/HP/.gemini/antigravity/brain/73bef1fa-b7ab-4dc9-b138-9fa87b4d2598/.system_generated/steps/21/output.txt', 'r', encoding='utf-8') as f:
    xml_content = ''.join([l for l in f if not l.startswith('IMPORTANT:')])

root = ET.fromstring(xml_content)

def print_tree(node, depth=0, max_depth=4):
    indent = '  ' * depth
    tag = node.tag
    nid = node.attrib.get('id', '')
    name = node.attrib.get('name', '')
    w = node.attrib.get('width', '')
    h = node.attrib.get('height', '')
    y = node.attrib.get('y', '')
    print(f'{indent}<{tag} id="{nid}" name="{name}" y="{y}" w="{w}" h="{h}"> ({len(node)} children)')
    if depth < max_depth:
        for child in node:
            print_tree(child, depth+1, max_depth)

print_tree(root, 0, 4)
