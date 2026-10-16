import os, subprocess

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

# Test 1: project.html scrolled to "The Problem" in default state
html_default = open('project.html', encoding='utf-8').read()
# scroll by putting element in view with scrollIntoView
scroll_default = '<script>window.addEventListener("DOMContentLoaded", () => { document.getElementById("problem-content").scrollIntoView(); });</script>'
html_default = html_default.replace('</body>', scroll_default + '</body>')
with open('scratch/test_project_default_scroll.html', 'w', encoding='utf-8') as f:
    f.write(html_default)

out1 = os.path.abspath('scratch/render_problem_default.png')
url1 = 'file:///' + os.path.abspath('scratch/test_project_default_scroll.html').replace('\\', '/')
subprocess.run([edge, '--headless=new', f'--screenshot={out1}', '--window-size=1200,600', url1], check=True)

# Test 2: project.html clicked Close on "The Problem"
click_script = '''
<script>
window.addEventListener("DOMContentLoaded", () => {
  const btns = document.querySelectorAll('.section-header__action');
  if (btns.length > 1) {
    btns[1].click(); // Closes "The Problem"
  }
  document.querySelector('.section-header h2').scrollIntoView();
});
</script>
'''
html_clicked = open('project.html', encoding='utf-8').read()
html_clicked = html_clicked.replace('</body>', click_script + '</body>')
with open('scratch/test_project_closed_scroll.html', 'w', encoding='utf-8') as f:
    f.write(html_clicked)

out2 = os.path.abspath('scratch/render_problem_closed.png')
url2 = 'file:///' + os.path.abspath('scratch/test_project_closed_scroll.html').replace('\\', '/')
subprocess.run([edge, '--headless=new', f'--screenshot={out2}', '--window-size=1200,600', url2], check=True)

print("Rendered without virtual time budget successfully")
