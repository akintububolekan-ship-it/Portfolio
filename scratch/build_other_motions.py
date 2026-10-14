import re

# Base template
with open('caterpillar.html', 'r', encoding='utf-8') as f:
    template = f.read()

# Build haystack-motion.html
haystack_html = template.replace('Caterpilllar Studios — Ola', 'Haystack Motion Design — Ola')

haystack_main = """
      <div class="project-content">
        <h1 class="project-title project-title--motion">
          Haystack | Product Introduction Video
        </h1>
        <div class="project-meta">
          <div class="project-meta__col">
            <span class="project-meta__label">Category</span>
            <span class="project-meta__value">Product Intro</span>
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
      <div class="project-content">
        <div class="project-text">
          <p>
            Haystack is an AI-powered customer service management tool. I designed and animated a product introduction video that highlights its core features, including chat automations, AI support, and ticketing systems.
          </p>
        </div>
      </div>
      <div class="project-image-container">
        <video src="images/Haystack Product Intro.mp4" autoplay loop muted playsinline class="project-image project-image--hero"></video>
      </div>
"""
# Replace main content in haystack
start = haystack_html.find('<!-- Top section: Title + Meta -->')
end = haystack_html.find('</main>')
if start != -1 and end != -1:
    haystack_html = haystack_html[:start] + haystack_main + '\n    ' + haystack_html[end:]
with open('haystack-motion.html', 'w', encoding='utf-8') as f:
    f.write(haystack_html)


# Build ifa-motion.html
ifa_html = template.replace('Caterpilllar Studios — Ola', 'IFA ai Launch Teaser — Ola')

ifa_main = """
      <div class="project-content">
        <h1 class="project-title project-title--motion">
          IFA ai | Launch Teaser
        </h1>
        <div class="project-meta">
          <div class="project-meta__col">
            <span class="project-meta__label">Category</span>
            <span class="project-meta__value">Launch Teaser</span>
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
      <div class="project-content">
        <div class="project-text">
          <p>
            IFA ai is a next-generation mobile AI assistant. For their initial release, I created a short, high-energy launch teaser that showcases the conversational intelligence and emotional resonance of the AI across various contexts.
          </p>
        </div>
      </div>
      <div class="project-image-container">
        <video src="images/ifa-launch-teaser.mp4" autoplay loop muted playsinline class="project-image project-image--hero"></video>
      </div>
"""
# Replace main content in ifa
start = ifa_html.find('<!-- Top section: Title + Meta -->')
end = ifa_html.find('</main>')
if start != -1 and end != -1:
    ifa_html = ifa_html[:start] + ifa_main + '\n    ' + ifa_html[end:]
with open('ifa-motion.html', 'w', encoding='utf-8') as f:
    f.write(ifa_html)
