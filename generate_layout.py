import os
import re

out_path = r'C:\Users\HP\.gemini\antigravity\brain\a5743cf2-2c8b-4925-9d8a-233014efb3cf\.system_generated\steps\15\output.txt'
lines = open(out_path, 'r', encoding='utf-8').read().split('\n')

elements = []
for line in lines:
    m = re.search(r'name="(Frame 1000005[0-9]+(-[0-9]+)?)"\s+x="([^"]+)"\s+y="([^"]+)"\s+width="([^"]+)"\s+height="([^"]+)"', line)
    if m:
        name = m.group(1)
        x = float(m.group(3))
        y = float(m.group(4))
        w = float(m.group(5))
        h = float(m.group(6))
        elements.append({'name': name, 'x': x, 'y': y, 'w': w, 'h': h})

unique = {}
for e in elements:
    unique[e['name']] = e

sorted_elements = sorted(unique.values(), key=lambda e: (round(e['y']/10)*10, e['x']))

html = '<div class="detailing-section">\n'

d = 'images/Haystack shorts'
svgs = [f for f in os.listdir(d) if f.endswith('.svg') and f.startswith('Frame ')]
available_frames = {f.replace('.svg', '') for f in svgs}

current_row = []
current_y = None

def render_row(row):
    if not row: return ""
    cols = len(row)
    if cols > 3: cols = 3 # cap to 3
    res = f'  <div class="detailing-row-{cols}">\n'
    for f in row:
        res += f'    <img src="images/Haystack shorts/{f}.svg" alt="{f}" />\n'
    res += '  </div>\n'
    return res

for e in sorted_elements:
    name = e['name']
    if name in available_frames:
        if current_y is None:
            current_y = round(e['y']/10)*10
        
        if abs(round(e['y']/10)*10 - current_y) > 10:
            html += render_row(current_row)
            current_row = []
            current_y = round(e['y']/10)*10
            
        current_row.append(name)

html += render_row(current_row)

# Append the videos section!
html += '  <div class="project-text"><h2>Video Assets</h2></div>\n'
html += '  <div class="detailing-row-3">\n'
for i in range(1, 8):
    html += f'    <video src="images/Haystack shorts/Video Project 9 ({i}).mp4" autoplay loop muted playsinline class="project-image" style="width: 100%; border-radius: 8px;"></video>\n'
html += '  </div>\n'

html += '</div>'

# Read haystack-motion.html
with open('haystack-motion.html', 'r', encoding='utf-8') as f:
    motion_html = f.read()

new_html = f"""      <div class="project-image-container">
        <video src="images/Haystack shorts/Video Project 9.mp4" autoplay loop muted playsinline class="project-image project-image--hero"></video>
      </div>

{html}"""

motion_html = re.sub(r'<div class="project-image-container">.*?</div>', new_html, motion_html, flags=re.DOTALL)

with open('haystack-motion.html', 'w', encoding='utf-8') as f:
    f.write(motion_html)

print("Updated haystack-motion.html!")
