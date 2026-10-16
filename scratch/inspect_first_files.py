import re

for f in ['articulate.html', 'articulate-project.html', 'bron.html', 'bron-project.html', 'baze-air.html', 'caterpillar.html']:
    content = open(f, encoding='utf-8').read()
    matches = re.findall(r'<button[^>]*onclick=[\"\']toggleSection\([\'\"](.*?)[\'\"],\s*this\)[\"\'][^>]*>(.*?)</button>', content, re.DOTALL)
    print(f"=== {f} ({len(matches)} sections) ===")
    for target_id, btn_text in matches:
        print(f"  Target: {target_id:25} | Button: {btn_text.strip():6}")
