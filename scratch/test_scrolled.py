import os, subprocess

base_html = open('index.html', encoding='utf-8').read()
base_html = base_html.replace('href="index.css"', 'href="../index.css"')
base_html = base_html.replace('src="images/', 'src="../images/')
base_html = base_html.replace('src="UI/', 'src="../UI/')

# Test with tabsWrapper sticky at top and cards scrolled behind it
test_html_2 = base_html.replace('</head>', '''
<style>
/* Simulate scrolled state where tabs-wrapper is fixed at top: 0 and content is scrolled underneath */
.bio, .hatched-divider {
  display: none !important;
}
.tabs-wrapper {
  background: #ffffff !important;
  pointer-events: auto !important;
}
</style>
</head>''')
test_html_2 = test_html_2.replace('if (bio) observer.observe(bio);', 'tabsWrapper.classList.add("is-sticky");')

with open('scratch/test_white_scrolled.html', 'w', encoding='utf-8') as f:
    f.write(test_html_2)

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
out2 = os.path.abspath('scratch/test_white_scrolled.png')
url2 = 'file:///' + os.path.abspath('scratch/test_white_scrolled.html').replace('\\', '/')
subprocess.run([edge, '--headless=new', f'--screenshot={out2}', '--window-size=1200,600', '--default-background-color=ffffff', url2], check=True)

print("Rendered test_white_scrolled")
