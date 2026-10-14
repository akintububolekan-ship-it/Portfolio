import sys
import xml.etree.ElementTree as ET

sys.stdout.reconfigure(encoding='utf-8')

path = r'C:\Users\HP\.gemini\antigravity\brain\f932e1f1-377b-4801-bc11-03730e9bdef2\.system_generated\steps\277\output.txt'
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    text = f.read()

# Check if there is an IMPORTANT notice at the end
clean_text = text.split('IMPORTANT:')[0].strip()

try:
    root = ET.fromstring(clean_text)
    print('Root:', root.tag, root.attrib)

    # Inspect children of Frame 87 (762:95436)
    f87 = root.find('.//*[@id="762:95436"]')
    if f87 is not None:
        print('f87 children:')
        for child in f87:
            print(' ', child.tag, child.attrib.get('id'), child.attrib.get('name'), child.attrib.get('y'), child.attrib.get('width'), child.attrib.get('height'))


except Exception as e:
    print('XML parse error:', e)
    # print lines
    lines = text.splitlines()
    for l in lines[:50]:
        print(l)
