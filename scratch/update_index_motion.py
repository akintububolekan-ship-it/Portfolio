import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

motion_section = """      <!-- Motion Design -->
      <section
        class="tab-content"
        id="content-motion-design"
        aria-label="Motion design projects"
      >
        <!-- Caterpilllar studio -->
        <a href="caterpillar.html" class="project-card" id="project-caterpillar">
          <div class="project-card__image-container">
            <video
              src="images/Caterpilllar images/Main video.mp4"
              autoplay loop muted playsinline
              class="project-card__image"
            ></video>
          </div>
          <div class="project-card__info">
            <h3 class="project-card__title">Caterpilllar studios</h3>
            <p class="project-card__desc">Product introduction video &amp; Storyboard</p>
          </div>
        </a>

        <!-- Haystack -->
        <a href="haystack-motion.html" class="project-card" id="project-haystack-motion">
          <div class="project-card__image-container">
            <video
              src="images/Haystack Product Intro.mp4"
              autoplay loop muted playsinline
              class="project-card__image"
            ></video>
          </div>
          <div class="project-card__info">
            <h3 class="project-card__title">Haystack</h3>
            <p class="project-card__desc">Product Introduction video</p>
          </div>
        </a>

        <!-- IFA ai -->
        <a href="ifa-motion.html" class="project-card" id="project-ifa-motion">
          <div class="project-card__image-container">
            <video
              src="images/ifa-launch-teaser.mp4"
              autoplay loop muted playsinline
              class="project-card__image"
            ></video>
          </div>
          <div class="project-card__info">
            <h3 class="project-card__title">IFA ai</h3>
            <p class="project-card__desc">Launch teaser</p>
          </div>
        </a>
      </section>"""

# Using regex to replace the section
pattern = re.compile(r'<!-- Motion Design -->\s*<section[^>]*id="content-motion-design"[^>]*>.*?</section>', re.DOTALL)
html = pattern.sub(motion_section, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
