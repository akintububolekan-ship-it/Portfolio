import os, subprocess

content = open('index.html', encoding='utf-8').read()
content = content.replace('href="index.css"', 'href="../index.css"')
content = content.replace('src="images/', 'src="../images/')
content = content.replace('src="UI/', 'src="../UI/')
content = content.replace('data-src-default="images/', 'data-src-default="../images/')
content = content.replace('data-src-hover="images/', 'data-src-hover="../images/')

# Add console logging of dither progress
content = content.replace('renderDither();', 'renderDither(); window.__ditherP = ditherProgress;')

test_script = '''
<script>
window.addEventListener("load", () => {
  setTimeout(() => {
    const avatar = document.getElementById("avatar");
    console.log("Triggering click on avatar");
    avatar.click();
  }, 400);
});
</script>
'''

content = content.replace('</body>', test_script + '</body>')

with open('scratch/test_avatar_mobile.html', 'w', encoding='utf-8') as f:
    f.write(content)

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

# Snapshot at 700ms (t = 400ms click + 300ms anim => ditherProgress should be 1.0)
out1 = os.path.abspath('scratch/render_avatar_revealed.png')
url = 'file:///' + os.path.abspath('scratch/test_avatar_mobile.html').replace('\\', '/')
subprocess.run([edge, '--headless=new', f'--screenshot={out1}', '--window-size=400,600', '--virtual-time-budget=750', url], check=True)

# Snapshot at 1600ms (t = 400ms click + 700ms wait + 300ms anim return + buffer => ditherProgress should be 0.0)
out2 = os.path.abspath('scratch/render_avatar_returned.png')
subprocess.run([edge, '--headless=new', f'--screenshot={out2}', '--window-size=400,600', '--virtual-time-budget=1600', url], check=True)

print("Both screenshots rendered successfully")
