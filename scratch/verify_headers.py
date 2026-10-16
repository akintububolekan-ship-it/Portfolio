import os, subprocess

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

html = open('project.html', encoding='utf-8').read()
html = html.replace('href="index.css"', 'href="../index.css"')
html = html.replace('src="images/', 'src="../images/')
html = html.replace('src="UI/', 'src="../UI/')

# 1. Mobile scrolled view
scroll_s = '<script>window.addEventListener("DOMContentLoaded", () => { window.scrollTo(0, 500); });</script>'
html_scrolled = html.replace('</body>', scroll_s + '</body>')
with open('scratch/verify_mobile_scrolled.html', 'w', encoding='utf-8') as f:
    f.write(html_scrolled)

out2 = os.path.abspath('scratch/verify_mobile_back_scrolled.png')
url_scrolled = 'file:///' + os.path.abspath('scratch/verify_mobile_scrolled.html').replace('\\', '/')
subprocess.run([edge, '--headless=new', f'--screenshot={out2}', '--window-size=390,700', url_scrolled], check=True)

# 2. Desktop scrolled view
scroll_d = '<script>window.addEventListener("DOMContentLoaded", () => { window.scrollTo(0, 500); });</script>'
html_desk = html.replace('</body>', scroll_d + '</body>')
with open('scratch/verify_desk_scrolled.html', 'w', encoding='utf-8') as f:
    f.write(html_desk)

out3 = os.path.abspath('scratch/verify_desk_back_scrolled.png')
url_desk = 'file:///' + os.path.abspath('scratch/verify_desk_scrolled.html').replace('\\', '/')
subprocess.run([edge, '--headless=new', f'--screenshot={out3}', '--window-size=1200,700', url_desk], check=True)

print("Updated renders complete")
