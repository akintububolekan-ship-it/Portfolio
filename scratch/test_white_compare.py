import os, subprocess

base_html = open('index.html', encoding='utf-8').read()
base_html = base_html.replace('href="index.css"', 'href="../index.css"')
base_html = base_html.replace('src="images/', 'src="../images/')
base_html = base_html.replace('src="UI/', 'src="../UI/')

# Test 1: background: #ffffff; with padding: 16px 0 36px;
# Test 2: background: #ffffff; with padding: 16px 0 20px; margin-bottom: 16px;
# Test 3: background: #ffffff; with padding: 16px 0 24px; margin-bottom: 12px;

# Let's create an inline style test for sticky state
# We can force sticky state by setting tabsWrapper to is-sticky and placing some mock cards behind it or scrolling
test_html_1 = base_html.replace('</head>', '''
<style>
.tabs-wrapper {
  background: #ffffff !important;
  pointer-events: auto !important;
}
</style>
</head>''')
test_html_1 = test_html_1.replace('if (bio) observer.observe(bio);', 'tabsWrapper.classList.add("is-sticky");')

with open('scratch/test_white_1.html', 'w', encoding='utf-8') as f:
    f.write(test_html_1)

edge = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
out1 = os.path.abspath('scratch/test_white_1.png')
url1 = 'file:///' + os.path.abspath('scratch/test_white_1.html').replace('\\', '/')
subprocess.run([edge, '--headless=new', f'--screenshot={out1}', '--window-size=1200,600', '--default-background-color=ffffff', url1], check=True)

print("Rendered test_white_1")
