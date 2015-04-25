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
	SEGMENTS = 7
	radius = hypot(x2-x1, y2-y1)/SEGMENTS
	theta = atan2(y2-y1, x2-x1)
	old_x = x1; old_y = y1
	for n in range(SEGMENTS):
		if random() < 0.8: theta += 0.2
		else: theta -= 0.2
		new_x = old_x + radius*cos(theta); new_y = old_y + radius*sin(theta)
		canvas.create_line(old_x, old_y, new_x, new_y, width = width, fill = kolor)
		old_x = new_x; old_y = new_y
	return new_x, new_y

def drawFlower(cx, cy, radius):
	#base case
	if radius < 3:
		return

	#set color
	kolor = 'GREEN'
	width = 2
	if radius < 120:
		kolor = 'WHITE'
		width = 1
	if radius < 10:
		kolor = 'RED'
		width = 1

	#draw flower
	for t in frange(0, 2*pi, 2*pi/7):
		x = cx + radius*sin(t)
		y = cy + radius*cos(t)
		new_x, new_y = drawLine(cx, cy, x, y, kolor, width)
		drawFlower(new_x, new_y, radius/3) #recurse

root = Tk()
canvas = setUpCanvas(root)
START_TIME = clock()

def main():
	drawFlower(WIDTH/2, HEIGHT/2 - 15, 240)
	displayStatistics()
	root.mainloop() #required for graphics

if __name__ == '__main__': main()