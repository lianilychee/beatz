from PIL import Image

im = Image.open("../images/piglet_color.jpg")
im.show()
pix = im.load()
[x,y] = im.size
print pix[100,100]