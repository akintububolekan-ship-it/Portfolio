import os, subprocess

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

# Test project.html default open state
out1 = os.path.abspath('scratch/render_project_default.png')
url1 = 'file:///' + os.path.abspath('project.html').replace('\\', '/')
subprocess.run([edge, '--headless=new', f'--screenshot={out1}', '--window-size=1200,800', url1], check=True)

# Test clicking close on 'problem-content' in project.html
test_click_html = open('project.html', encoding='utf-8').read()
click_script = '''
<script>
window.addEventListener("load", () => {
  // Click on the first Close button (Design process) and second (The Problem)
  const btns = document.querySelectorAll('.section-header__action');
  if (btns.length > 1) {
    btns[1].click(); // Closes "The Problem"
  }
});
</script>
'''
test_click_html = test_click_html.replace('</body>', click_script + '</body>')
with open('scratch/test_project_click.html', 'w', encoding='utf-8') as f:
    f.write(test_click_html)

out2 = os.path.abspath('scratch/render_project_closed.png')
url2 = 'file:///' + os.path.abspath('scratch/test_project_click.html').replace('\\', '/')
subprocess.run([edge, '--headless=new', f'--screenshot={out2}', '--window-size=1200,800', '--virtual-time-budget=500', url2], check=True)

print("Rendered project default and closed states successfully")
