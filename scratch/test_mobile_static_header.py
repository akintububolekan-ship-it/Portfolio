import os, subprocess

content = open('project.html', encoding='utf-8').read()
content = content.replace('href="index.css"', 'href="../index.css"')
content = content.replace('src="images/', 'src="../images/')
content = content.replace('src="UI/', 'src="../UI/')

test_style = '''
<style>
@media (max-width: 768px) {
  .project-header {
    position: static !important;
    background: none !important;
    padding-bottom: 0 !important;
    height: auto !important;
    pointer-events: auto !important;
  }
  .project-header__inner {
    padding: 24px 24px 0 !important;
  }
}
</style>
'''
content = content.replace('</head>', test_style + '</head>')

# Top view
with open('scratch/test_mobile_static_top.html', 'w', encoding='utf-8') as f:
    f.write(content)

# Scrolled view (e.g. scroll down 500px)
# Use scrollIntoView to reliably scroll in headless Edge
scroll_s = '<script>window.addEventListener("DOMContentLoaded", () => { document.querySelector(".project-image--hero").scrollIntoView(); });</script>'
content_scrolled = content.replace('</body>', scroll_s + '</body>')
with open('scratch/test_mobile_static_scrolled.html', 'w', encoding='utf-8') as f:
    f.write(content_scrolled)

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

out1 = os.path.abspath('scratch/render_static_top.png')
url1 = 'file:///' + os.path.abspath('scratch/test_mobile_static_top.html').replace('\\', '/')
subprocess.run([edge, '--headless=new', f'--screenshot={out1}', '--window-size=390,700', url1], check=True)

out2 = os.path.abspath('scratch/render_static_scrolled.png')
url2 = 'file:///' + os.path.abspath('scratch/test_mobile_static_scrolled.html').replace('\\', '/')
subprocess.run([edge, '--headless=new', f'--screenshot={out2}', '--window-size=390,700', url2], check=True)

print("Rendered properly styled mobile static header tests")
