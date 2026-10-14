import os
import imageio.v3 as iio

# Let's check text or content in each video
files = [
    '202610120028.mp4',
    '202610120028 (1).mp4',
    '202610120028 (2).mp4',
    '202610120028 (3).mp4',
    '202610120028 (4).mp4',
    '202610120028 (5).mp4'
]

d = 'images/Haystack shorts'
for f in files:
    path = os.path.join(d, f)
    # read frame at 1 sec
    frame = iio.imread(path, index=15)
    print(f"{f}: duration={iio.immeta(path).get('duration', 'unknown')}, size={os.path.getsize(path)}")
