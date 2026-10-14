import imageio_ffmpeg, subprocess, json

ffmpeg_exe = imageio_ffmpeg.get_ffmpeg_exe()
vids = [
    'images/Haystack shorts/202610120028 (5).mp4',
    'images/Haystack shorts/Video Project 9 (6).mp4',
    'images/Haystack shorts/Video Project 9 (7).mp4',
]
for v in vids:
    cmd = [ffmpeg_exe, '-i', v]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    for line in res.stderr.splitlines():
        if 'Stream #0:0' in line or 'Duration' in line:
            print(v, line.strip())
