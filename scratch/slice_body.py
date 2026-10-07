from PIL import Image
Image.MAX_IMAGE_PIXELS = None

im = Image.open('images/Articulate Images/Body.png')
w, h = im.size
print("Body size:", w, h)

# In Body.png, let's take 6 vertical slices of 5000px height each:
# 0..5000, 5000..10000, 10000..15000, 15000..20000, 20000..25000, 25000..32768
step = 5500
for i in range(0, h, step):
    y_end = min(i + step, h)
    slice_img = im.crop((0, i, w, y_end))
    # resize down to width 800 for quick visual inspection
    r_h = int((y_end - i) * (800 / w))
    thumb = slice_img.resize((800, r_h), Image.Resampling.LANCZOS)
    thumb.save(f'scratch/body_thumb_{i}.png')
    print(f"Saved scratch/body_thumb_{i}.png (y: {i}..{y_end})")
