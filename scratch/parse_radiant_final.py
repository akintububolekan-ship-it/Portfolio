import xml.etree.ElementTree as ET

path = r"C:\Users\HP\.gemini\antigravity\brain\f932e1f1-377b-4801-bc11-03730e9bdef2\.system_generated\steps\454/output.txt"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

text_xml = text.split("IMPORTANT:")[0].strip()
root = ET.fromstring(text_xml)

def find_node(node, id_val):
    if node.attrib.get('id') == id_val:
        return node
    for ch in node:
        res = find_node(ch, id_val)
        if res is not None:
            return res
    return None

final_frame = find_node(root, "762:109187")
if final_frame is not None:
    print(f"Direct children of {final_frame.attrib.get('name')} ({final_frame.attrib.get('id')}):")
    for ch in final_frame:
        print(f"  {ch.tag} id={ch.attrib.get('id')} name='{ch.attrib.get('name')}' width={ch.attrib.get('width')} height={ch.attrib.get('height')}")
else:
    print("Not found")
