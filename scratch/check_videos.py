import os
import glob

# Check video files
print("Checking files...")
folders = [
    r"C:\Users\HP\Downloads\Portfolio\images\Caterpilllar images",
    r"C:\Users\HP\Downloads\Portfolio\images",
    r"C:\Users\HP\Downloads\AEUX_0.8.2\AEUX_0.8.2\Figma\Public work display",
    r"C:\Users\HP\Downloads\AEUX_0.8.2\AEUX_0.8.2\Figma\Public work display\Adobe After Effects Auto-Save"
]

for folder in folders:
    print(f"\n--- {folder} ---")
    if os.path.exists(folder):
        for f in os.listdir(folder):
            if f.lower().endswith(('.mp4', '.mov', '.avi', '.webm')):
                path = os.path.join(folder, f)
                size_mb = os.path.getsize(path) / (1024 * 1024)
                print(f"  {f} ({size_mb:.2f} MB)")
