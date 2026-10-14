import re

with open('caterpillar.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The section we want to replace starts with "<!-- Product Storyboard -->"
# and ends right before "</main>"
start_index = html.find('<!-- Product Storyboard -->')
end_index = html.find('</main>')

if start_index != -1 and end_index != -1:
    new_detailing_section = """<!-- Detailing -->
      <div class="project-content">
        <div class="project-text">
          <h2>Detailing</h2>
        </div>
      </div>

      <!-- Detailing Grid Sequence -->
      <div class="detailing-section">
        <!-- 1 image -->
        <div class="detailing-row-1">
          <img src="images/project-3.png" alt="Detailing placeholder 1" />
        </div>
        <!-- 3 images -->
        <div class="detailing-row-3">
          <img src="images/project-3.png" alt="Detailing placeholder 2" />
          <img src="images/project-3.png" alt="Detailing placeholder 3" />
          <img src="images/project-3.png" alt="Detailing placeholder 4" />
        </div>
        <!-- 3 images -->
        <div class="detailing-row-3">
          <img src="images/project-3.png" alt="Detailing placeholder 5" />
          <img src="images/project-3.png" alt="Detailing placeholder 6" />
          <img src="images/project-3.png" alt="Detailing placeholder 7" />
        </div>
        <!-- 2 images -->
        <div class="detailing-row-2">
          <img src="images/project-3.png" alt="Detailing placeholder 8" />
          <img src="images/project-3.png" alt="Detailing placeholder 9" />
        </div>
        <!-- 1 image -->
        <div class="detailing-row-1">
          <img src="images/project-3.png" alt="Detailing placeholder 10" />
        </div>
      </div>
"""
    # Create the new HTML
    new_html = html[:start_index] + new_detailing_section + "\n    " + html[end_index:]
    
    with open('caterpillar.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Replaced successfully.")
else:
    print("Could not find start/end bounds.")
