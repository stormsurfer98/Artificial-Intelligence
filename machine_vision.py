#Name: Shrey Gupta
#Date: March 2015
#Period: 4

from tkinter import *
from math import pi, sqrt, sin, cos, tan, radians, atan2
from copy import copy

HEIGHT = 0; WIDTH = 0
root = Tk()

class ImageFrame:
	def __init__(self, image, COLORFLAG = False):
		self.img = PhotoImage(width = WIDTH, height = HEIGHT)
		for row in range(HEIGHT):
			for col in range(WIDTH):
				num = image[row*WIDTH + col]
				if COLORFLAG == True:
					kolor = '#%02x%02x%02x' % (num[0], num[1], num[2]) #color
				else:
					kolor = '#%02x%02x%02x' % (num, num, num) #gray-scale
				self.img.put(kolor, (col, row))
		c = Canvas(root, width = WIDTH, height = HEIGHT); c.pack()
		c.create_image(0, 0, image = self.img, anchor = NW)

def displayImageInWindow(image):
	global x
	x = ImageFrame(image)

def drawCircle(image, x, y, r):
	for i in range(x - r, x + r + 1):
		for j in range(y - r, y + r + 1):
			if 0 <= i < HEIGHT and 0 <= j < WIDTH:
				if round(sqrt((x-i)**2 + (y-j)**2)) == r:
					image[j*WIDTH + i] = 126

def loadImage():
	f = open('shapes-image.txt', 'r')
	ppm = f.readline().strip("\n")
	size = f.readline().strip("\n").split(" ")
	maxColor = f.readline().strip("\n")
	image = f.read().split()
	for n in range(len(image)):
		image[n] = int(image[n])
	global WIDTH; global HEIGHT
	WIDTH = int(size[0]); HEIGHT = int(size[1])
	return image

def grayScale(image):
	grayScaleImage = []
	for pos in range(0, len(image), 3):
		RGB = (int(image[pos+0]), int(image[pos+1]), int(image[pos+2]))
		grayScaleImage.append(int(0.2*RGB[0] + 0.7*RGB[1] + 0.1*RGB[2]))
	return grayScaleImage

def blurImage(image):
	blurredImage = [255] * WIDTH * HEIGHT
	for row in range(1, HEIGHT-1):
		for col in range(1, WIDTH-1):
			imageSum = 0
			imageSum += image[(row-1)*WIDTH + (col-1)]
			imageSum += 2*image[(row)*WIDTH + (col-1)]
			imageSum += image[(row+1)*WIDTH + (col-1)]
			imageSum += 2*image[(row-1)*WIDTH + (col)]
			imageSum += 4*image[(row)*WIDTH + (col)]
			imageSum += 2*image[(row+1)*WIDTH + (col)]
			imageSum += image[(row-1)*WIDTH + (col+1)]
			imageSum += 2*image[(row)*WIDTH + (col+1)]
			imageSum += image[(row+1)*WIDTH + (col+1)]
			blurredImage[row*WIDTH + col] = int(1/16*imageSum)
	return blurredImage

def sobelMask(image):
	sobelArray = [0] * WIDTH * HEIGHT
	for row in range(1, HEIGHT-1):
		for col in range(1, WIDTH-1):
			Gx = 0; Gy = 0
			Gy += image[(row-1)*WIDTH + (col-1)]
			Gy += 2*image[(row)*WIDTH + (col-1)]
			Gy += image[(row+1)*WIDTH + (col-1)]
			Gy -= image[(row-1)*WIDTH + (col+1)]
			Gy -= 2*image[(row)*WIDTH + (col+1)]
			Gy -= image[(row+1)*WIDTH + (col+1)]
			Gx -= image[(row-1)*WIDTH + (col-1)]
			Gx -= 2*image[(row-1)*WIDTH + (col)]
			Gx -= image[(row-1)*WIDTH + (col+1)]
			Gx += image[(row+1)*WIDTH + (col-1)]
			Gx += 2*image[(row+1)*WIDTH + (col)]
			Gx += image[(row+1)*WIDTH + (col+1)]
			m = sqrt(Gx*Gx + Gy*Gy); t = atan2(Gy, Gx)
			sobelArray[row*WIDTH + col] = [m, t, 255*(m < 75), False]
	return sobelArray

def fixCellAt(image, row, col):
	if row <= 1 or row >= HEIGHT-2 or col <= 1 or col >= WIDTH-2: return
	if image[row*WIDTH + col][3] == True or image[row*WIDTH + col][0] < 75: return
	else:
		image[row*WIDTH + col][3] = True
		t = radians(int(45*round(float(image[row*WIDTH + col][1])/45)))
		moveRow = round(sin(t))
		moveCol = round(cos(t))
		if 0 <= row + moveRow < HEIGHT and 0 <= col + moveCol < WIDTH:
			fixCellAt(image, row + moveRow, col + moveCol)
			if(image[(row+moveRow)*WIDTH + (col+moveCol)][0] <= image[row*WIDTH + col][0]):
				image[(row+moveRow)*WIDTH + (col+moveCol)][2] = 255
			else:
				image[row*WIDTH + col][2] = 255
		if 0 <= row - moveRow < HEIGHT and 0 <= col - moveCol < WIDTH:
			fixCellAt(image, row - moveRow, col - moveCol)
			if(image[(row-moveRow)*WIDTH + (col-moveCol)][0] <= image[row*WIDTH + col][0]):
				image[(row-moveRow)*WIDTH + (col-moveCol)][2] = 255
			else:
				image[row*WIDTH + col][2] = 255	

def cannyTransform(sobelArray):
	cannyArray = copy(sobelArray)
	for row in range(1, HEIGHT-1):
		for col in range(1, WIDTH-1):
			if cannyArray[row*WIDTH + col][0] < 75: #cell is NOT a structural edge point
				cannyArray[row*WIDTH + col][3] = True
			else:
				fixCellAt(cannyArray, row, col) #edge will be thinned
	return cannyArray

def extractImage(cannyArray):
	cannyImage = [255] * WIDTH * HEIGHT
	for row in range(1, HEIGHT-1):
		for col in range(1, WIDTH-1):
			cannyImage[row*WIDTH + col] = cannyArray[row*WIDTH + col][2]
	return cannyImage

def findOriginalEdge(cannyArray, row, col):
	for n in range(col, WIDTH-1):
		if cannyArray[row*WIDTH + n][2] == 0:
			return abs(n - col)

def circleDetection(image, cannyArray):
	votes = [0] * WIDTH * HEIGHT
	for row in range(1, HEIGHT-1):
		for col in range(1, WIDTH-1):
			if cannyArray[row*WIDTH + col][2] == 0:
				m = tan(pi/2 + cannyArray[row*WIDTH + col][1])
				for n in range(-WIDTH, WIDTH):
					if 0 <= round(row+m*n) < HEIGHT and 0 <= (col+n) < WIDTH:
						votes[round(row+m*n)*WIDTH + (col+n)] += 1
	circleImage = copy(image)
	for row in range(1, HEIGHT-1):
		for col in range(1, WIDTH-1):
			if votes[row*WIDTH + col] >= 50:
				radius = findOriginalEdge(cannyArray, row, col)
				drawCircle(circleImage, row, col, radius)
	return circleImage

def main():
	image = loadImage()
	grayScaleImage = grayScale(image)
	blurredImage = copy(grayScaleImage)
	for x in range(5): blurredImage = blurImage(blurredImage)
	sobelArray = sobelMask(blurredImage)
	cannyArray = cannyTransform(sobelArray)
	cannyImage = extractImage(cannyArray)
	circleImage = circleDetection(grayScaleImage, cannyArray)
	displayImageInWindow(circleImage)
	root.mainloop()

main()