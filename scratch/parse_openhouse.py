import re
import xml.etree.ElementTree as ET

path = r"C:\Users\HP\.gemini\antigravity\brain\f932e1f1-377b-4801-bc11-03730e9bdef2\.system_generated\steps\412\output.txt"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

text_xml = text.split("IMPORTANT:")[0].strip()
root = ET.fromstring(text_xml)

print(f"Root: {root.tag} id={root.attrib.get('id')} name='{root.attrib.get('name')}'")

def print_tree(node, depth=0, max_depth=3):
    indent = "  " * depth
    print(f"{indent}<{node.tag} id='{node.attrib.get('id')}' name='{node.attrib.get('name')}' w={node.attrib.get('width')} h={node.attrib.get('height')}>")
    if depth < max_depth:
        for ch in node:
            print_tree(ch, depth + 1, max_depth)

print_tree(root, 0, 4)
