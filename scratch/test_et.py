import xml.etree.ElementTree as ET
import re

with open(r'C:\Users\HP\.gemini\antigravity\brain\7a5e906f-81a6-45aa-836b-28f86646166b\.system_generated\steps\53\output.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace any unescaped & with &amp; if needed, or fix xml
# Let's clean text to make it valid xml
# Note: & is already &amp; or &#39; in most places.
try:
    root = ET.fromstring(text)
    print("Parsed directly with ElementTree! Root tag:", root.tag, root.attrib)
except Exception as e:
    print("ET error:", e)
