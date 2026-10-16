import glob, re

for f in ['bron.html', 'bron-project.html', 'ifa.html', 'ifa-project.html', 'articulate.html', 'articulate-project.html', 'project.html', 'rihub.html', 'sprance.html', 'sprance-project.html']:
    content = open(f, encoding='utf-8').read()
    h2s = re.findall(r'<h2[^>]*>(.*?)</h2>', content)
    print(f"=== {f} ===")
    for h in h2s:
        if any(w in h.lower() for w in ['final', 'design', 'screen', 'solution', 'wireframe', 'paper']):
            print("  ", h)
