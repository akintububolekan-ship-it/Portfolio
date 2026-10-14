import re

new_block = '''<!-- Information Architecture -->
      <div class="project-content">
        <div class="project-text project-text--has-image">
          <h2>Information Architecture</h2>
          <p>
            <a
              href="https://www.figma.com/board/gy9ofwmEFy2Th2CnqPnkZR/Untitled?node-id=7-31&t=ymyrgd06mrBK1gdV-4"
              target="_blank"
              rel="noopener noreferrer"
              >View on figma</a
            >
          </p>
        </div>
      </div>

      <!-- Information Architecture Image -->
      <img
        src="images/UI/Bron IA.svg"
        alt="Information Architecture"
        class="project-image"
      />

      <!-- The Final Design -->'''

for filename in ['bron.html', 'bron-project.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    updated, count = re.subn(r'<!-- Information Architecture -->.*?<!-- The Final Design -->', new_block, content, flags=re.DOTALL)
    if count == 1:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(updated)
        print(f'Successfully updated {filename}')
    else:
        print(f'Failed to match in {filename}, count={count}')
