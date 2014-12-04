''' This snippet of code tests the feasibility of iterating through the image matrix to determine where the hand is.
'''

from PIL import Image

im = Image.open("../images/black_background_red_dot.jpg")
# im = Image.open("../images/green.jpg")
im.show()
pix = im.load()
[x,y] = im.size

# print [x,y]

# Important note: iterating through a 1920 x 1080 image takes a minute and a half.

# Iterate through matrix of pixels
for i in range (x):
	for j in range (y):
		[pixR, pixG, pixB] = pix[i,j]
		if pixR > 50:
			print 'RED IDENTIFIED'
		else:
			print 'no red'

