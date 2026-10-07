import os
import subprocess

edge_paths = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
]

edge_exe = None
for p in edge_paths:
    if os.path.exists(p):
        edge_exe = p
        break

if edge_exe:
    url = "file:///" + os.path.abspath("articulate.html").replace("\\", "/")
    out_img = os.path.abspath("scratch/articulate_render.png")
    cmd = [
        edge_exe,
        "--headless=new",
        f"--screenshot={out_img}",
        "--window-size=1200,2400",
        "--default-background-color=ffffff",
        url
    ]
    subprocess.run(cmd, check=True)
    print("Rendered successfully:", out_img, os.path.exists(out_img))
else:
    print("Edge executable not found.")
