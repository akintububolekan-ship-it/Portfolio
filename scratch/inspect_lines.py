import imageio.v3 as iio
import numpy as np

img = iio.imread(r'C:/Users/HP/.gemini/antigravity/brain/a5743cf2-2c8b-4925-9d8a-233014efb3cf/.user_uploaded/media_1791770620460_66ca0079.png')

# Find horizontal lines where brightness spikes across the entire width
for y in range(len(img)):
    row = img[y, :, :3]
    # check if there are white pixels across the row
    bright = np.sum(row > 150)
    if bright > 50:
        print(f"y={y}: {bright} bright pixels, median={np.median(row)}")
