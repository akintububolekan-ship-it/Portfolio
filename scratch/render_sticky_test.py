import os, subprocess

content = open('index.html', encoding='utf-8').read()
content = content.replace('href="index.css"', 'href="../index.css"')
content = content.replace('src="images/', 'src="../images/')
content = content.replace('src="UI/', 'src="../UI/')
content = content.replace('if (bio) observer.observe(bio);', 'tabsWrapper.classList.add("is-sticky"); // if (bio) observer.observe(bio);')
with open('scratch/test_sticky_bar.html', 'w', encoding='utf-8') as f:
    f.write(content)

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
out = os.path.abspath('scratch/render_sticky_bar.png')
url = 'file:///' + os.path.abspath('scratch/test_sticky_bar.html').replace('\\', '/')
subprocess.run([edge, '--headless=new', f'--screenshot={out}', '--window-size=1200,600', '--default-background-color=ffffff', url], check=True)
print("Rendered forced sticky bar")
