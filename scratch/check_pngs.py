import os
import imageio.v3 as iio
import numpy as np

for f in sorted(os.listdir('scratch')):
    if f.startswith('202610120028') and f.endswith('.png'):
        img = iio.imread(os.path.join('scratch', f))
        print(f, "shape:", img.shape, "mean:", np.mean(img, axis=(0,1)).astype(int))
