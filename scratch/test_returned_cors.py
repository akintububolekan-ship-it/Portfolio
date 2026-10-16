import os, subprocess

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
url = 'file:///' + os.path.abspath('scratch/test_avatar_mobile.html').replace('\\', '/')

# At t = 1600ms (t = 400ms click + 700ms wait + 300ms return + 200ms buffer => returned to default)
out2 = os.path.abspath('scratch/render_avatar_returned_cors.png')
subprocess.run([edge, '--headless=new', '--allow-file-access-from-files', f'--screenshot={out2}', '--window-size=400,600', '--virtual-time-budget=1600', url], check=True)
print("Rendered returned with allow-file-access-from-files")
