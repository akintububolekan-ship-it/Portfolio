import os
import imageio.v3 as iio
import numpy as np

img = iio.imread('scratch/202610120028.png')
print('Top row mean:', np.mean(img[0, :, :]))
print('Bottom row mean:', np.mean(img[-1, :, :]))
print('Left col mean:', np.mean(img[:, 0, :]))
print('Right col mean:', np.mean(img[:, -1, :]))
