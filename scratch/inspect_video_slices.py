import os
import imageio.v3 as iio
import numpy as np

for f in sorted(os.listdir('scratch')):
    if f.startswith('202610120028') and f.endswith('.png'):
        img = iio.imread(os.path.join('scratch', f))
        # Top area where title might be
        top_slice = img[:150, :, :]
        # Check some colors/brightness
        print(f"{f}:")
        print(f"  top brightness: {np.mean(top_slice):.1f}")
        print(f"  left vs right brightness: left={np.mean(img[:, :576]):.1f}, right={np.mean(img[:, 576:]):.1f}")
