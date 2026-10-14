import os
import imageio.v3 as iio

d = 'images/Haystack shorts'
for f in sorted(os.listdir(d)):
    if f.endswith('.mp4'):
        path = os.path.join(d, f)
        try:
            frames = iio.imread(path, index=0)
            print(f, frames.shape)
        except Exception as e:
            print(f, 'Error:', e)
