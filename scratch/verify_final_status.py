import glob, re

# Check all HTML files with toggleSection
files = sorted(glob.glob('*.html'))

all_ok = True
for f in files:
    content = open(f, encoding='utf-8').read()
    if 'function toggleSection' not in content:
        continue
    
    # check that no 'View' buttons exist
    views = re.findall(r'<button[^>]*class=[\"\']section-header__action[\"\'][^>]*>\s*View\s*</button>', content)
    closes = re.findall(r'<button[^>]*class=[\"\']section-header__action[\"\'][^>]*>\s*Close\s*</button>', content)
    
    # check that no target elements have display: none inline
    target_ids = re.findall(r'toggleSection\([\'\"](.*?)[\'\"],', content)
    hidden_ids = []
    for tid in target_ids:
        tag_m = re.search(r'<[^>]+id=[\"\']' + re.escape(tid) + r'[\"\'][^>]*>', content)
        if tag_m and 'display: none' in tag_m.group(0):
            hidden_ids.append(tid)
            
    print(f"{f:25} | Closes: {len(closes):2} | Views: {len(views):2} | Hidden targets: {len(hidden_ids)}")
    if len(views) > 0 or len(hidden_ids) > 0:
        all_ok = False

print(f"\nFinal Verification Status: {'ALL CLEAN' if all_ok else 'ISSUES FOUND'}")
