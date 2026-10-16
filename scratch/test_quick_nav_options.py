import os, subprocess

html_base = open('project.html', encoding='utf-8').read()

# Option 1: bottom-centered floating pill
style_opt1 = '''
<style>
.quick-nav-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.38);
  backdrop-filter: blur(2px);
  -webkit-backdrop-filter: blur(2px);
  z-index: 998;
  pointer-events: auto;
}
.quick-nav-pill {
  position: fixed;
  bottom: 48px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 999;
  display: inline-flex;
  align-items: center;
  gap: 10px;
  padding: 10px 18px 10px 12px;
  background: #111111;
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 9999px;
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.35), 0 2px 6px rgba(0, 0, 0, 0.2);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  font-size: 14px;
  font-weight: 500;
  cursor: pointer;
  white-space: nowrap;
}
.quick-nav-pill__arrow {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.15);
}
.quick-nav-pill__arrow svg {
  width: 14px;
  height: 14px;
  stroke: #ffffff;
}
.quick-nav-pill__close {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  color: rgba(255, 255, 255, 0.5);
  background: none;
  border: none;
  margin-left: 2px;
  cursor: pointer;
}
</style>
'''

pill_html = '''
<div class="quick-nav-backdrop"></div>
<button class="quick-nav-pill">
  <span class="quick-nav-pill__arrow">
    <svg viewBox="0 0 24 24" fill="none" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
      <path d="M12 4v14M5 13l7 7 7-7" />
    </svg>
  </span>
  <span>Click to scroll to final design</span>
  <span class="quick-nav-pill__close">&times;</span>
</button>
'''

html_opt1 = html_base.replace('</head>', style_opt1 + '</head>').replace('</body>', pill_html + '</body>')
with open('scratch/test_opt1_bottom.html', 'w', encoding='utf-8') as f:
    f.write(html_opt1)

# Option 2: mid-screen centered
style_opt2 = style_opt1.replace('bottom: 48px;', 'top: 45%; transform: translate(-50%, -50%);')
html_opt2 = html_base.replace('</head>', style_opt2 + '</head>').replace('</body>', pill_html + '</body>')
with open('scratch/test_opt2_center.html', 'w', encoding='utf-8') as f:
    f.write(html_opt2)

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

# Render Option 1 Desktop & Mobile
subprocess.run([edge, '--headless=new', f'--screenshot={os.path.abspath("scratch/render_opt1_desk.png")}', '--window-size=1200,800', 'file:///' + os.path.abspath('scratch/test_opt1_bottom.html').replace('\\', '/')], check=True)
subprocess.run([edge, '--headless=new', f'--screenshot={os.path.abspath("scratch/render_opt1_mobile.png")}', '--window-size=390,700', 'file:///' + os.path.abspath('scratch/test_opt1_bottom.html').replace('\\', '/')], check=True)

# Render Option 2 Desktop & Mobile
subprocess.run([edge, '--headless=new', f'--screenshot={os.path.abspath("scratch/render_opt2_desk.png")}', '--window-size=1200,800', 'file:///' + os.path.abspath('scratch/test_opt2_center.html').replace('\\', '/')], check=True)
subprocess.run([edge, '--headless=new', f'--screenshot={os.path.abspath("scratch/render_opt2_mobile.png")}', '--window-size=390,700', 'file:///' + os.path.abspath('scratch/test_opt2_center.html').replace('\\', '/')], check=True)

print("Rendered all option comparisons")
