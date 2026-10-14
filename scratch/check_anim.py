import imageio_ffmpeg, subprocess

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
for t in [0.5, 1.5, 2.5, 3.5, 4.5]:
    out = f"scratch/202610120028_5_t{t}.jpg"
    cmd = [ffmpeg_exe, '-y', '-ss', str(t), '-i', 'images/Haystack shorts/202610120028 (5).mp4', '-vframes', '1', out]
    subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Extracted t={t}")
