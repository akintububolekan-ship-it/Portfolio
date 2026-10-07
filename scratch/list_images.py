import os
import glob

files = glob.glob(r'c:\Users\HP\Downloads\Portfolio\images\**\*.*', recursive=True)
for f in sorted(files):
    if not f.endswith('.py') and not f.endswith('.txt'):
        print(f"{os.path.basename(f)}  ({os.path.getsize(f)} bytes)")
