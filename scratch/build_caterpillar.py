import re

with open('caterpillar.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Also fix the page title
html = html.replace('<title>Haystack Case Study — Ola</title>', '<title>Caterpilllar Studios — Ola</title>')

new_main = """
      <!-- Top section: Title + Meta -->
      <div class="project-content">
        <h1 class="project-title project-title--motion">
          Caterpilllar studios | Product introduction video &amp; Product Storyboard
        </h1>

        <div class="project-meta">
          <div class="project-meta__col">
            <span class="project-meta__label">Category</span>
            <span class="project-meta__value">3D Arts</span>
          </div>
          <div class="project-meta__col">
            <span class="project-meta__label">Year</span>
            <span class="project-meta__value">2024</span>
          </div>
          <div class="project-meta__col">
            <span class="project-meta__label">My role</span>
            <span class="project-meta__value">Motion designer</span>
          </div>
        </div>
      </div>

      <!-- Overview -->
      <div class="project-content">
        <div class="project-text">
          <p>
            Caterpillar studio is an upcoming 3D arts and illustration studio in Germany, when they launched they reached out to me for a product introduction video and to create a 3D animated storyboard for a film they had in the works.
          </p>
        </div>
      </div>

      <!-- Overview Hero Video -->
      <div class="project-image-container">
        <video src="images/Caterpilllar images/Main video.mp4" autoplay loop muted playsinline class="project-image project-image--hero"></video>
      </div>

      <!-- Features -->
      <div class="project-content">
        <div class="project-text">
          <h2>Features</h2>
          <div class="features-list">
            <div class="feature-item">AE</div>
            <div class="feature-item">Cinema 4D</div>
            <div class="feature-item">Premiere pro</div>
            <div class="feature-item">Illustrator</div>
            <div class="feature-item">Photoshop</div>
            <div class="feature-item">Ai</div>
          </div>
        </div>
      </div>

      <!-- Video Assets -->
      <div class="project-content">
        <div class="project-text">
          <h2>Video Assets</h2>
          <p>Here is a flow of scenes directly taken from the video sequence, below is</p>
        </div>
      </div>
      <img src="images/Caterpilllar images/storyboard-grid.png" alt="Storyboard Grid" class="project-image" />

      <!-- Animation Storyboard -->
      <div class="project-content">
        <div class="project-text">
          <h2>Animation storyboard</h2>
        </div>
      </div>

      <!-- Storyboard Videos -->
      <div class="storyboard-videos">
        <div class="storyboard-item">
          <div class="storyboard-number">1</div>
          <video src="images/Caterpilllar images/Video Project 8 (1).mp4" autoplay loop muted playsinline></video>
        </div>
        <div class="storyboard-item">
          <div class="storyboard-number">2</div>
          <video src="images/Caterpilllar images/Video Project 8 (2).mp4" autoplay loop muted playsinline></video>
        </div>
        <div class="storyboard-item">
          <div class="storyboard-number">3</div>
          <video src="images/Caterpilllar images/Video Project 8 (3).mp4" autoplay loop muted playsinline></video>
        </div>
        <div class="storyboard-item">
          <div class="storyboard-number">4</div>
          <video src="images/Caterpilllar images/Video Project 8 (4).mp4" autoplay loop muted playsinline></video>
        </div>
        <div class="storyboard-item">
          <div class="storyboard-number">5</div>
          <video src="images/Caterpilllar images/Video Project 8 (5).mp4" autoplay loop muted playsinline></video>
        </div>
        <div class="storyboard-item">
          <div class="storyboard-number">6</div>
          <video src="images/Caterpilllar images/Video Project 8 (6).mp4" autoplay loop muted playsinline></video>
        </div>
      </div>
"""

html = html.replace('<!-- CONTENT -->', new_main)

with open('caterpillar.html', 'w', encoding='utf-8') as f:
    f.write(html)
