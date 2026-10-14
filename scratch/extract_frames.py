import os, glob, subprocess
import imageio_ffmpeg

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
videos = glob.glob('images/Haystack shorts/*.mp4')
for v in videos:
    base = os.path.basename(v).replace(' ', '_').replace('(', '').replace(')', '').replace('.mp4', '')
    out_path = f"scratch/{base}.jpg"
    cmd = [ffmpeg_exe, '-y', '-ss', '00:00:01', '-i', v, '-vframes', '1', out_path]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Extracted {v} -> {out_path} (exists={os.path.exists(out_path)})")
