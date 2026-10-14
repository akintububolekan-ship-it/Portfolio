import re

with open('haystack-motion.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_html = """      <div class="project-image-container">
        <video src="images/Haystack shorts/Video Project 9.mp4" autoplay loop muted playsinline class="project-image project-image--hero"></video>
      </div>

      <div class="detailing-section">
        <!-- Videos grid -->
        <div class="detailing-row-3">
          <video src="images/Haystack shorts/Video Project 9 (1).mp4" autoplay loop muted playsinline class="project-image" style="width: 100%; border-radius: 8px;"></video>
          <video src="images/Haystack shorts/Video Project 9 (2).mp4" autoplay loop muted playsinline class="project-image" style="width: 100%; border-radius: 8px;"></video>
          <video src="images/Haystack shorts/Video Project 9 (3).mp4" autoplay loop muted playsinline class="project-image" style="width: 100%; border-radius: 8px;"></video>
        </div>
        <div class="detailing-row-3">
          <video src="images/Haystack shorts/Video Project 9 (4).mp4" autoplay loop muted playsinline class="project-image" style="width: 100%; border-radius: 8px;"></video>
          <video src="images/Haystack shorts/Video Project 9 (5).mp4" autoplay loop muted playsinline class="project-image" style="width: 100%; border-radius: 8px;"></video>
          <video src="images/Haystack shorts/Video Project 9 (6).mp4" autoplay loop muted playsinline class="project-image" style="width: 100%; border-radius: 8px;"></video>
        </div>
        <div class="detailing-row-1">
          <video src="images/Haystack shorts/Video Project 9 (7).mp4" autoplay loop muted playsinline class="project-image" style="width: 100%; border-radius: 8px;"></video>
        </div>
      </div>"""

html = re.sub(r'<div class="project-image-container">.*?</div>', new_html, html, flags=re.DOTALL)

with open('haystack-motion.html', 'w', encoding='utf-8') as f:
    f.write(html)
