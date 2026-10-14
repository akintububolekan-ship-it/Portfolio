import os
import imageio.v3 as iio
import numpy as np

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
    frame = iio.imread(path, index=15)
    # Check if there is blue, yellow, green
    # Integrations has colorful logos: Stripe (purple/blue), Flutterwave (orange), Gmail (red/blue), iMessage (green)
    # Messages has blue and red badges (e.g. red notification 3, 12)
    # Chat screen has blue chat bubbles!
    blue_pixels = np.sum((frame[:, :, 2] > 100) & (frame[:, :, 0] < 50))
    red_pixels = np.sum((frame[:, :, 0] > 100) & (frame[:, :, 2] < 50))
    print(f"{f}: blue={blue_pixels}, red={red_pixels}")
