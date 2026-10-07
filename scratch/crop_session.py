from PIL import Image
Image.MAX_IMAGE_PIXELS = None

im = Image.open('images/Articulate Images/Body.png')
w, h = im.size

# Let's crop from y=5000 to y=8500 (in 14845 scale)
y1 = int(h * (5000 / 14845))
y2 = int(h * (7000 / 14845))
crop = im.crop((0, y1, w, y2))
crop.save('scratch/crop_session_flow.png')
print("Saved scratch/crop_session_flow.png")
