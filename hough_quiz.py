#Name: Shrey Gupta
#Date: March 10, 2015
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

def drawLineMB(m, b, image):
	for x in range(WIDTH):
		index = WIDTH * round(m * x + b) + x
		if 0 <= index < len(image):
			image[index] = 255

def main():
	image = [0] * HEIGHT * WIDTH
	for theta in range(-90, 96, 6):
		m = tan(radians(theta))
		b = 256 - 256*tan(radians(theta))
		drawLineMB(m, b, image)
	displayImageInWindow(image)
	root.mainloop()

main()