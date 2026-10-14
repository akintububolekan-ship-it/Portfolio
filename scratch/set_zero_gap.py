# Add .project-image-group--no-gap to index.css
with open('index.css', 'r', encoding='utf-8') as f:
    css = f.read()

if '.project-image-group--no-gap' not in css:
    target = '.project-image-group .project-image {'
    replacement = '.project-image-group--no-gap {\n  gap: 0;\n}\n\n.project-image-group .project-image {'
    css = css.replace(target, replacement, 1)
    with open('index.css', 'w', encoding='utf-8') as f:
        f.write(css)
    print('Updated index.css')

# Update haystack-motion.html
with open('haystack-motion.html', 'r', encoding='utf-8') as f:
    html = f.read()

target_html = '<div class="project-image-group">'
replacement_html = '<div class="project-image-group project-image-group--no-gap" style="gap: 0;">'
if target_html in html:
    html = html.replace(target_html, replacement_html, 1)
    with open('haystack-motion.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('Updated haystack-motion.html')
else:
    print('Target not found in haystack-motion.html')
