from PIL import Image
import subprocess, os

svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 18" width="16" height="18" fill="#111">
  <path fill-rule="evenodd" clip-rule="evenodd" d="M3 0C1.895 0 1 0.895 1 2V16C1 17.105 1.895 18 3 18H13C14.105 18 15 17.105 15 16V5L10 0H3ZM8 4.5C6.895 4.5 6 5.395 6 6.5C6 7.605 6.895 8.5 8 8.5C9.105 8.5 10 7.605 10 6.5C10 5.395 9.105 4.5 8 4.5ZM4 14C4 11.8 5.8 10.5 8 10.5C10.2 10.5 12 11.8 12 14C12 14.5 11.6 15 11 15H5C4.4 15 4 14.5 4 14Z" fill="#111"/>
</svg>'''

with open('scratch/resume_icon_v2.svg', 'w') as f:
    f.write(svg)
print("Saved resume_icon_v2.svg")
