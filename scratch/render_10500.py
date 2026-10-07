import os
import subprocess

edge_exe = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
url = "file:///" + os.path.abspath("sprance.html").replace("\\", "/")
out_img = os.path.abspath("scratch/sprance_full_10500.png")
cmd = [
    edge_exe,
    "--headless=new",
    f"--screenshot={out_img}",
    "--window-size=1200,10500",
    "--default-background-color=ffffff",
    url
]
subprocess.run(cmd, check=True)
print("Rendered 10500 successfully")
