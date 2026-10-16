import os, subprocess

html = open('project.html', encoding='utf-8').read()

# Let's test scrollIntoView on #final-design
test_scroll = '''
<script>
window.addEventListener("DOMContentLoaded", () => {
  const h2s = document.querySelectorAll('h2');
  let target = null;
  for (let h of h2s) {
    if (/final\s*design/i.test(h.textContent)) {
      target = h;
      break;
    }
  }
  if (target) {
    target.id = 'final-design';
    target.style.scrollMarginTop = '90px';
    target.scrollIntoView({ behavior: 'auto', block: 'start' });
  }
});
</script>
'''

test_page = html.replace('</body>', test_scroll + '</body>')
with open('scratch/test_scroll_target.html', 'w', encoding='utf-8') as f:
    f.write(test_page)

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

out_desk = os.path.abspath('scratch/render_scrolled_to_final_desk.png')
url = 'file:///' + os.path.abspath('scratch/test_scroll_target.html').replace('\\', '/')
subprocess.run([edge, '--headless=new', f'--screenshot={out_desk}', '--window-size=1200,800', url], check=True)

out_mob = os.path.abspath('scratch/render_scrolled_to_final_mob.png')
subprocess.run([edge, '--headless=new', f'--screenshot={out_mob}', '--window-size=390,700', url], check=True)

print("Rendered target landing position")
