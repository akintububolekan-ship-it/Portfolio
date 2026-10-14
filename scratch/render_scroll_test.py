import os, subprocess

content = open('index.html', encoding='utf-8').read()
content = content.replace('href="index.css"', 'href="../index.css"')
content = content.replace('src="images/', 'src="../images/')
content = content.replace('src="UI/', 'src="../UI/')
scroll_script = '''
<script>
window.addEventListener("DOMContentLoaded", () => {
    setTimeout(() => {
        window.scrollTo(0, 800);
    }, 100);
});
</script>
'''
content = content.replace('</body>', scroll_script + '</body>')

with open('scratch/test_sticky_scroll.html', 'w', encoding='utf-8') as f:
    f.write(content)

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
out = os.path.abspath('scratch/render_scroll_current.png')
url = 'file:///' + os.path.abspath('scratch/test_sticky_scroll.html').replace('\\', '/')
# wait a bit for js
subprocess.run([edge, '--headless=new', f'--screenshot={out}', '--window-size=1200,600', '--default-background-color=ffffff', '--run-all-compositor-stages-before-draw', '--virtual-time-budget=2000', url], check=True)
print('Done render_scroll_current')
