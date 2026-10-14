new_css = """
/* Haystack Motion Detailing Multi-Video Grids */
.detailing-grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1px;
  background: rgba(255, 255, 255, 0.2);
  border-top: 1px solid rgba(255, 255, 255, 0.2);
  width: 100%;
  box-sizing: border-box;
}

.detailing-grid-2 video,
.detailing-grid-2 .project-image {
  width: 100%;
  height: 100%;
  aspect-ratio: 320 / 235;
  object-fit: cover;
  display: block;
  background: #000;
  padding: 0;
  margin: 0;
  border-radius: 0;
}

.detailing-grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1px;
  background: rgba(255, 255, 255, 0.2);
  border-top: 1px solid rgba(255, 255, 255, 0.2);
  width: 100%;
  box-sizing: border-box;
}

.detailing-grid-3 video,
.detailing-grid-3 .project-image {
  width: 100%;
  height: 100%;
  aspect-ratio: 213 / 156;
  object-fit: cover;
  display: block;
  background: #000;
  padding: 0;
  margin: 0;
  border-radius: 0;
}
"""

with open('index.css', 'r', encoding='utf-8') as f:
    css = f.read()

if '.detailing-grid-2' not in css:
    css = css.strip() + '\n' + new_css
    with open('index.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print("Updated index.css with detailing-grid rules")

# Now update haystack-motion.html
with open('haystack-motion.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Insert Row 1 (2 videos) and Row 2 (3 videos) inside .project-image-group
grid_html = """          <div class="detailing-grid-2">
            <video
              src="images/Haystack shorts/202610120028.mp4"
              autoplay
              loop
              muted
              playsinline
              class="project-image"
            ></video>
            <video
              src="images/Haystack shorts/202610120028 (1).mp4"
              autoplay
              loop
              muted
              playsinline
              class="project-image"
            ></video>
          </div>
          <div class="detailing-grid-3">
            <video
              src="images/Haystack shorts/202610120028 (2).mp4"
              autoplay
              loop
              muted
              playsinline
              class="project-image"
            ></video>
            <video
              src="images/Haystack shorts/202610120028 (3).mp4"
              autoplay
              loop
              muted
              playsinline
              class="project-image"
            ></video>
            <video
              src="images/Haystack shorts/202610120028 (4).mp4"
              autoplay
              loop
              muted
              playsinline
              class="project-image"
            ></video>
          </div>"""

target_video = """          <video
            src="images/Haystack shorts/Video Project 9 (2).mp4"
            autoplay
            loop
            muted
            playsinline
            class="project-image"
          ></video>"""

if target_video in html:
    new_block = target_video + '\n' + grid_html
    html = html.replace(target_video, new_block, 1)
    with open('haystack-motion.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated haystack-motion.html with the video grids")
else:
    print("Target video not found in haystack-motion.html!")
