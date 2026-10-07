import xml.etree.ElementTree as ET

with open(r'C:\Users\HP\.gemini\antigravity\brain\7a5e906f-81a6-45aa-836b-28f86646166b\.system_generated\steps\53\output.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

xml_text = "".join(lines[:-1])
root = ET.fromstring(xml_text)

def dump_node(node, depth=0):
    indent = "  " * depth
    info = f"<{node.tag} id='{node.attrib.get('id')}' name='{node.attrib.get('name')}' y='{node.attrib.get('y')}'>"
    texts = []
    for t in node.findall('.//text'):
        texts.append(t.attrib.get('name', ''))
    
    # print summary of direct children
    print(f"{indent}{info} -> {len(texts)} texts. First few: {texts[:3]}")
    for child in node:
        if depth < 5:
            dump_node(child, depth + 1)

dump_node(root)
