import os, subprocess

html = open('project.html', encoding='utf-8').read()

# Polished quick nav CSS
nav_css = '''
<style>
.quick-nav-backdrop {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.42);
  backdrop-filter: blur(2.5px);
  -webkit-backdrop-filter: blur(2.5px);
  z-index: 998;
  opacity: 1;
  transition: opacity 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  cursor: pointer;
}

.quick-nav-pill {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 999;
  display: inline-flex;
  align-items: center;
  gap: 12px;
  padding: 12px 20px 12px 14px;
  background: #111111;
  color: #ffffff;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 9999px;
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.35), 0 4px 12px rgba(0, 0, 0, 0.2);
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  font-size: 14.5px;
  font-weight: 500;
  letter-spacing: -0.01em;
  cursor: pointer;
  white-space: nowrap;
  user-select: none;
  -webkit-tap-highlight-color: transparent;
  transition: transform 0.2s ease, background-color 0.2s ease, box-shadow 0.2s ease;
}

.quick-nav-pill:hover {
  background: #1f1f1f;
  transform: translate(-50%, -52%);
  box-shadow: 0 20px 48px rgba(0, 0, 0, 0.45);
}

.quick-nav-pill__arrow {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.14);
  flex-shrink: 0;
  animation: qnBounce 1.5s ease-in-out infinite;
}

.quick-nav-pill__arrow svg {
  width: 15px;
  height: 15px;
  stroke: #ffffff;
  stroke-width: 2.2;
}

.quick-nav-pill__text {
  color: #ffffff;
  line-height: 1;
}

.quick-nav-pill__close {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  margin-left: 4px;
  color: rgba(255, 255, 255, 0.45);
  background: none;
  border: none;
  cursor: pointer;
  font-size: 16px;
  line-height: 1;
  transition: color 0.15s ease, background 0.15s ease;
}

.quick-nav-pill__close:hover {
  color: #ffffff;
  background: rgba(255, 255, 255, 0.15);
}

@keyframes qnBounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(3px); }
}

@media (max-width: 480px) {
  .quick-nav-pill {
    padding: 10px 16px 10px 12px;
    font-size: 13.5px;
    gap: 9px;
    max-width: calc(100vw - 36px);
  }
  .quick-nav-pill__arrow {
    width: 24px;
    height: 24px;
  }
}
</style>
'''

nav_html = '''
<div class="quick-nav-backdrop" id="quick-nav-backdrop"></div>
<button class="quick-nav-pill" id="quick-nav-pill">
  <span class="quick-nav-pill__arrow">
    <svg viewBox="0 0 24 24" fill="none" stroke-linecap="round" stroke-linejoin="round">
      <path d="M12 4v14M5 13l7 7 7-7" />
    </svg>
  </span>
  <span class="quick-nav-pill__text">Click to scroll to final design</span>
  <span class="quick-nav-pill__close" id="quick-nav-close" aria-label="Dismiss">&times;</span>
</button>
'''

test_page = html.replace('</head>', nav_css + '</head>').replace('</body>', nav_html + '</body>')
with open('scratch/test_styled_nav.html', 'w', encoding='utf-8') as f:
    f.write(test_page)

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'

out_desk = os.path.abspath('scratch/render_nav_desk.png')
url = 'file:///' + os.path.abspath('scratch/test_styled_nav.html').replace('\\', '/')
subprocess.run([edge, '--headless=new', f'--screenshot={out_desk}', '--window-size=1200,800', url], check=True)

out_mob = os.path.abspath('scratch/render_nav_mob.png')
subprocess.run([edge, '--headless=new', f'--screenshot={out_mob}', '--window-size=390,700', url], check=True)

print("Rendered polished test nav")
