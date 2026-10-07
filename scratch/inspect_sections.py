import re

with open(r'C:\Users\HP\.gemini\antigravity\brain\7a5e906f-81a6-45aa-836b-28f86646166b\.system_generated\steps\53\output.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's see all lines with <frame or <text or <instance or <component
# specifically let's track the depth / tree of elements under frame id="432:20919"
lines = text.splitlines()

stack = []
for i, line in enumerate(lines):
    indent = len(line) - len(line.lstrip())
    stripped = line.strip()
    if stripped.startswith('<frame'):
        # extract id and name
        m = re.search(r'id="([^"]+)" name="([^"]+)"', stripped)
        if m:
            fid, fname = m.groups()
            # print up to level 4
            level = indent // 2
            if level <= 4:
                print(f"{'  '*level}[{fid}] {fname}")
    elif stripped.startswith('<text'):
        m = re.search(r'id="([^"]+)" name="([^"]+)"', stripped)
        if m:
            fid, tname = m.groups()
            level = indent // 2
            if level <= 4:
                print(f"{'  '*level}TEXT: {tname[:60]}")
