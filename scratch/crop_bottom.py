from PIL import Image
Image.MAX_IMAGE_PIXELS = None

im = Image.open('images/Articulate Images/Body.png')
w, h = im.size

# Let's crop from y=11500 to 14845
y1 = int(h * (11500 / 14845))
crop = im.crop((0, y1, w, h))
crop.save('scratch/crop_bottom.png')
print("Saved scratch/crop_bottom.png")
