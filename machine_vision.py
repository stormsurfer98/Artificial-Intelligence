#Name: Shrey Gupta
#Date: March 2015
#Period: 4

from tkinter import *
from random import randint
from math import sqrt, cos, tan, radians
from copy import copy

HEIGHT = 0
WIDTH = 0
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

def loadImage():
	f = open('team-rocket.txt', 'r')
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

def main():
	image = loadImage()
	grayScaleImage = grayScale(image)
	blurredImage = copy(grayScaleImage)
	for x in range(6): blurredImage = blurImage(blurredImage)
	displayImageInWindow(blurredImage)
	root.mainloop()

main()