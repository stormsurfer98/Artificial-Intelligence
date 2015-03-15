#Name: Shrey Gupta
#Date: March 3, 2015
#Period: 1

from tkinter import *
from random import randint
from math import sqrt, cos, tan, radians

HEIGHT = 512
WIDTH = 512
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

def imageNoise(points, image):
	for n in range(points):
		r = randint(0, HEIGHT - 1)
		c = randint(0, WIDTH - 1)
		image[WIDTH * r + c] = 255

def drawLineMB(m, b, image):
	for x in range(WIDTH):
		index = WIDTH * round(m * x + b) + x
		if 0 <= index < len(image):
			image[index] = 255

def drawLineRT(r, t, image):
	m = tan(radians(t)); b = r/cos(90 - radians(t))
	drawLineMB(m, b, image)

def drawCircle(x, y, r, image):
	for i in range(x - r, x + r + 1):
		for j in range(y - r, y + r + 1):
			if round(sqrt((x-i)**2 + (y-j)**2)) == r:
				image[WIDTH * j + i] = 255

def main():
	image = [0] * HEIGHT * WIDTH
	imageNoise(500, image)
	drawLineMB(0, 256, image)
	drawLineMB(1, 0, image)
	drawLineRT(5, 30, image)
	drawCircle(256, 256, 200, image)
	displayImageInWindow(image)
	root.mainloop()

main()
