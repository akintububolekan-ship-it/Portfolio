from PIL import Image
Image.MAX_IMAGE_PIXELS = None

im = Image.open('images/Articulate Images/Body.png')
w, h = im.size

# Let's crop from y=3600 to y=4200 (in 14845 scale)
y1 = int(h * (3600 / 14845))
y2 = int(h * (4200 / 14845))
crop = im.crop((0, y1, w, y2))
crop.save('scratch/crop_paper_wireframes.png')
print("Saved scratch/crop_paper_wireframes.png")
