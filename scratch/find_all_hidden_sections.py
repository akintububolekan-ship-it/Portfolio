import glob, re

files = sorted(glob.glob('*.html'))
found_hidden = []
for f in files:
    content = open(f, encoding='utf-8').read()
    # Find all toggleSection target IDs
    target_ids = re.findall(r'toggleSection\([\'\"](.*?)[\'\"],', content)
    for tid in target_ids:
        # find the element with id=tid
        elem_match = re.search(r'<[^>]+id=[\"\']' + re.escape(tid) + r'[\"\'][^>]*>', content)
        if elem_match:
            tag = elem_match.group(0)
            if 'display' in tag and 'none' in tag:
                found_hidden.append((f, tid, tag))
            elif 'hidden' in tag:
                found_hidden.append((f, tid, tag))

print(f"Total hidden section targets found: {len(found_hidden)}")
for item in found_hidden:
    print(item)
