import os, subprocess

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
out1 = os.path.abspath('scratch/render_avatar_revealed_cors.png')
url = 'file:///' + os.path.abspath('scratch/test_avatar_mobile.html').replace('\\', '/')
subprocess.run([edge, '--headless=new', '--allow-file-access-from-files', f'--screenshot={out1}', '--window-size=400,600', '--virtual-time-budget=800', url], check=True)
print("Rendered with allow-file-access-from-files")
