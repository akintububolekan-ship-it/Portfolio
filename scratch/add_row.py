import re

with open('caterpillar.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add the final row
addition = """        <!-- 3 images (Bottom row from image) -->
        <div class="detailing-row-3">
          <img src="images/project-3.png" alt="Detailing placeholder 11" />
          <img src="images/project-3.png" alt="Detailing placeholder 12" />
          <img src="images/project-3.png" alt="Detailing placeholder 13" />
        </div>
      </div>
"""
html = html.replace('      </div>\n\n    </main>', addition + '\n    </main>')

with open('caterpillar.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated")
