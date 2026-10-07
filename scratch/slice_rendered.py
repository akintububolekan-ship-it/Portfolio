from PIL import Image

img = Image.open('scratch/sprance_full_render.png')
w, h = img.size
print(f"Rendered dimensions: {w}x{h}")

# Crop into 4 slices
slice_h = h // 4
for i in range(4):
    box = (0, i * slice_h, w, min(h, (i + 1) * slice_h))
    crop = img.crop(box)
    crop.save(f'scratch/check_render_slice_{i}.png')
print("Saved 4 check render slices")
