from PIL import Image
Image.MAX_IMAGE_PIXELS = None

im = Image.open('images/Articulate Images/Body.png')
w, h = im.size
print(f"Image size: {w}x{h}")

# In Figma: Frame 1000005340 starts around y=250.36, height=12568.66.
# Section 6 (Information architecture) is at y=3434 in Figma.
# Let's find relative position:
# In Figma, total frame height is 14845.
# 3434 / 14845 ≈ 0.2313
# Let's crop from y_start = int(h * (3300 / 14845)) to y_end = int(h * (3800 / 14845))
y1 = int(h * (3350 / 14845))
y2 = int(h * (3800 / 14845))
crop = im.crop((0, y1, w, y2))
crop.save('scratch/crop_info_arch.png')
print("Saved scratch/crop_info_arch.png, size:", crop.size)
