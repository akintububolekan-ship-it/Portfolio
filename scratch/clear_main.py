import re

with open('caterpillar.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_main = html.find('<main class="project-page">')
end_main = html.find('</main>')
if start_main != -1 and end_main != -1:
    html = html[:start_main + len('<main class="project-page">')] + '\n<!-- CONTENT -->\n    ' + html[end_main:]

with open('caterpillar.html', 'w', encoding='utf-8') as f:
    f.write(html)
