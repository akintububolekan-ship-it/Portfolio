from PIL import Image

im = Image.open(r'c:\Users\HP\Downloads\Portfolio\images\Body.png')
print("Image size:", im.size)

# The image is 1263 x 14845
# Let's crop y from 600 to 2000 (where Problem, Goal, Research, etc. are) and check
crop = im.crop((0, 600, 1263, 2000))
crop.save(r'c:\Users\HP\Downloads\Portfolio\scratch\crop_top.png')
print("Saved crop_top.png")
