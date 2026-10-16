import glob, re

files = sorted(glob.glob('*.html'))
for f in files:
    content = open(f, encoding='utf-8').read()
    if 'section-header__action' not in content:
        continue
    
    matches = re.findall(r'<button[^>]*onclick=[\"\']toggleSection\([\'\"](.*?)[\'\"],\s*this\)[\"\'][^>]*>(.*?)</button>', content, re.DOTALL)
    print(f"=== {f} ({len(matches)} sections) ===")
    for target_id, btn_text in matches:
        btn_clean = btn_text.strip()
        target_match = re.search(r'id=[\"\']' + re.escape(target_id) + r'[\"\'][^>]*>', content)
        target_tag = target_match.group(0) if target_match else 'NOT FOUND'
        is_hidden = 'display' in target_tag and 'none' in target_tag
        print(f"  Target: {target_id:25} | Button: {btn_clean:6} | Hidden: {is_hidden} | Tag: {target_tag}")
