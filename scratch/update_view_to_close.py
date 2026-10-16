import re

# Update project.html
p_content = open('project.html', encoding='utf-8').read()
# In project.html, buttons are:
# <button class="section-header__action" onclick="toggleSection('...', this)">View</button>
p_updated = re.sub(
    r'(<button class="section-header__action" onclick="toggleSection\([\'\"].*?[\'\"],\s*this\)">)View(</button>)',
    r'\1Close\2',
    p_content
)
with open('project.html', 'w', encoding='utf-8') as f:
    f.write(p_updated)
print("Updated project.html")

# Update bron.html
b_content = open('bron.html', encoding='utf-8').read()
b_updated = re.sub(
    r'(<button\s+class="section-header__action"\s+onclick="toggleSection\([\'\"].*?[\'\"],\s*this\)"\s*>\s*)View(\s*</button>)',
    r'\1Close\2',
    b_content
)
with open('bron.html', 'w', encoding='utf-8') as f:
    f.write(b_updated)
print("Updated bron.html")

# Update bron-project.html
bp_content = open('bron-project.html', encoding='utf-8').read()
bp_updated = re.sub(
    r'(<button\s+class="section-header__action"\s+onclick="toggleSection\([\'\"].*?[\'\"],\s*this\)"\s*>\s*)View(\s*</button>)',
    r'\1Close\2',
    bp_content
)
with open('bron-project.html', 'w', encoding='utf-8') as f:
    f.write(bp_updated)
print("Updated bron-project.html")
