import os

for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.mp4'):
            p = os.path.join(root, f)
            print(p, os.path.getsize(p))
