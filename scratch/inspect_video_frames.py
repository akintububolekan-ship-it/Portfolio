import os
import imageio.v3 as iio
import numpy as np

d = 'images/Haystack shorts'
videos = [f for f in sorted(os.listdir(d)) if f.endswith('.mp4')]

for v in videos:
    path = os.path.join(d, v)
    try:
        # Read a frame near middle of video
        frame = iio.imread(path, index=10)
        # Check average brightness and some features
        print(f"{v}: shape={frame.shape}, mean_rgb={np.mean(frame, axis=(0,1)).astype(int)}")
    except Exception as e:
        print(f"{v}: error={e}")
