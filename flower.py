#Name: Shrey Gupta
#Date: March 2015
#Period: 1

from tkinter import Tk, Canvas, YES, BOTH
from time import clock
from random import random
from math import sin, cos, atan2, pi, hypot

WIDTH = 1275 #root.winfo_screenwidth()
HEIGHT = 685 #root.winfo_screenheight()

def setUpCanvas(root):
	root.title("FRACTAL FLOWERS by Shrey Gupta")
	canvas = Canvas(root, width = WIDTH, height = HEIGHT, bg = 'BLACK')
	canvas.pack(expand = YES, fill = BOTH)
	return canvas

def displayStatistics():
	print('RUN TIME =%6.2f'% round(clock()-START_TIME, 2), 'seconds.')
	root.title('The fractal flower is complete.')

def frange(start, stop, step):
	i = start
	while i < stop:
		yield i
		i += step

def drawLine(x1, y1, x2, y2, kolor = 'WHITE', width = 1):
	radius = hypot(x2-x1, y2-y1)/7
	x_step = (x2-x1)/7; y_step = (y2-y1)/7
	theta = atan2(y2-y1, x2-x1)
	for n in range(0, 7):
		if random() < 0.8: new_theta = theta + 0.2
		else: new_theta = theta - 0.2
		new_x = x1 + n*x_step + radius*cos(new_theta)
		new_y = y1 + n*y_step + radius*sin(new_theta)
		canvas.create_line(x1 + n*x_step, y1 + n*y_step, new_x, new_y, width = width, fill = kolor)

def drawFlower(cx, cy, radius):
	#base case
	if radius < 3:
		return

	#set color
	kolor = 'GREEN'
	width = 2
	if radius == clock():
		kolor = 'WHITE'
		width = 1
	if radius < 10:
		kolor = 'RED'
		width = 1

	#draw flower
	for t in frange(0, 2*pi, 2*pi/7):
		x = cx + radius*sin(t)
		y = cy + radius*cos(t)
		drawLine(cx, cy, x, y, kolor, width)
		drawFlower(x, y, radius/3) #recurse

root = Tk()
canvas = setUpCanvas(root)
START_TIME = clock()

def main():
	drawFlower(WIDTH/2, HEIGHT/2 - 15, 240)
	displayStatistics()
	root.mainloop() #required for graphics

if __name__ == '__main__': main()