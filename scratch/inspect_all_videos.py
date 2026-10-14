import os, glob
import imageio.v3 as iio

videos = glob.glob('images/**/*.mp4', recursive=True)
for v in videos:
    try:
        props = iio.improps(v, plugin='pyav')
        print(f"{v}: shape={props.shape}, n_images={props.n_images}")
        # Save frame 0
        frame = iio.imread(v, index=0, plugin='pyav')
        out_name = os.path.basename(v).replace(' ', '_').replace('(', '').replace(')', '') + '.png'
        iio.imwrite(os.path.join('scratch', out_name), frame)
        print(f"  Saved thumbnail scratch/{out_name}")
    except Exception as e:
        print(f"{v}: error {e}")
