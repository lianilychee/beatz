''' This snippet of code tests the feasibility of iterating through the image matrix to determine where the hand is.

	This implies that we are using color recognition to determine hand location.  Lindsey is testing mean shift on old contoured images.
'''

from PIL import Image

im = Image.open("../images/piglet_color.jpg")
im.show()
pix = im.load()
[x,y] = im.size
# print pix[100,100]

# Iterate through matrix of pixels
for i in range (x):
	# print i
	for j in range (y):
		# print j
		print pix[i,j]