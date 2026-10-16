import glob, re

css_content = ""
for f in glob.glob('*.css'):
    css_content += open(f, encoding='utf-8').read() + "\n"

html_files = sorted(glob.glob('*.html'))
target_ids = set()
for f in html_files:
    content = open(f, encoding='utf-8').read()
    ids = re.findall(r'toggleSection\([\'\"](.*?)[\'\"],', content)
    target_ids.update(ids)

print(f"Target IDs found ({len(target_ids)}): {target_ids}")
hidden_in_css = []
for tid in target_ids:
    if f"#{tid}" in css_content:
        print(f"ID #{tid} found in CSS!")
        # check if it sets display
        m = re.search(r'#' + re.escape(tid) + r'[\s\S]*?\}', css_content)
        if m and 'display' in m.group(0):
            print(f"  Rules: {m.group(0)}")

print("CSS check complete")
