import os, subprocess

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

# Test 1: project.html mobile top
out1 = os.path.abspath('scratch/mobile_header_top.png')
url1 = 'file:///' + os.path.abspath('project.html').replace('\\', '/')
subprocess.run([edge, '--headless=new', f'--screenshot={out1}', '--window-size=390,700', url1], check=True)

# Test 2: project.html mobile scrolled
html = open('project.html', encoding='utf-8').read()
scroll_s = '<script>window.addEventListener("DOMContentLoaded", () => { window.scrollTo(0, 400); });</script>'
html = html.replace('</body>', scroll_s + '</body>')
with open('scratch/test_mobile_scroll.html', 'w', encoding='utf-8') as f:
    f.write(html)

out2 = os.path.abspath('scratch/mobile_header_scrolled.png')
url2 = 'file:///' + os.path.abspath('scratch/test_mobile_scroll.html').replace('\\', '/')
subprocess.run([edge, '--headless=new', f'--screenshot={out2}', '--window-size=390,700', url2], check=True)

print("Rendered mobile header top and scrolled")
