import os
import imageio.v3 as iio

d = 'images/Haystack shorts'
new_videos = [f for f in sorted(os.listdir(d)) if f.startswith('202610120028') and f.endswith('.mp4')]

for v in new_videos:
    path = os.path.join(d, v)
    try:
        frame = iio.imread(path, index=10)
        out_name = os.path.join('scratch', v.replace('.mp4', '.png'))
        iio.imwrite(out_name, frame)
        print(f"Saved {out_name}: shape={frame.shape}")
    except Exception as e:
        print(f"{v}: error={e}")
