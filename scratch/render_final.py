import os, subprocess

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
out = os.path.abspath('scratch/render_final_white.png')
url = 'file:///' + os.path.abspath('index.html').replace('\\', '/')
subprocess.run([edge, '--headless=new', f'--screenshot={out}', '--window-size=1200,800', '--default-background-color=ffffff', url], check=True)
print("Rendered final index")
