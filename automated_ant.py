#Name: Shrey Gupta
#Date: February 2015
#Period: 1

from tkinter import Tk, Canvas, YES, BOTH
from time import clock
from random import choice

def setUpCanvas(root):
	root.title("The AUTOMATIC ANT by Shrey Gupta")
	canvas = Canvas(root, width = SCREEN_WIDTH, height = SCREEN_HEIGHT, bg = 'BLACK')
	canvas.pack(expand = YES, fill = BOTH)
	return canvas

def placeFrameAroundWindow():
	canvas.create_rectangle(5, 5, SCREEN_WIDTH, SCREEN_HEIGHT, width = 1, outline = 'GOLD')

def displayStatistics(startTime):
	elapsedTime = round(clock()-startTime, 2)
	speedPerThousand = round(1000*elapsedTime/STEPS, 2)
	print('+==========< Automated Ant Statistics >==========+')
	print('ANT MOVES =', STEPS, 'steps.')
	print('RUN TIME =%6.2f'% elapsedTime, 'seconds.')
	print('SPEED =%6.2f'% speedPerThousand, 'seconds-per-1000-moves.')
	message = 'PROGRAM DONE. Final image is ' + str(STEPS) + ' ant moves in ' + str(elapsedTime) + ' seconds.'
	root.title(message)

def displayMatrix(matrix): #used for debugging
	print('MATRIX:')
	for row in matrix:
		[print (x, ' ', end = '') for x in row]
		print()

def plot(x, y, kolor = 'WHITE'): #plots 5x5 "points" on video screen
	canvas.create_rectangle(x, y, x+5, y+5, width = 1, fill = kolor)

def createPixelWorld():
	#size matrix (the pixel world)
	ROW = SCREEN_HEIGHT*2
	COL = SCREEN_WIDTH*2

	#fill world with cells all the same color: white (0)
	matrix = [[0 for c in range(COL)] for r in range(ROW)]

	#place ant in pixel world (ant[0] = 0 means ant moves up)
	placeFrameAroundWindow()
	ant = [0, ANT_START_ROW, ANT_START_COL]
	return ant, matrix

def move(ant): #move ant forward to next cell
	direction = ant[0]
	if direction % 360 == 0:
		ant[2] += 5
	elif direction % 360 == 180:
		ant[2] -= 5
	elif direction % 360 == 90:
		ant[1] += 5
	elif direction % 360 == 270:
		ant[1] -= 5
	
	#wrap around, if necessary
	if ant[1] > SCREEN_WIDTH: #ant[1] = COL
		ant[1] = 5
	if ant[1] < 5:
		ant[1] = SCREEN_WIDTH
	if ant[2] > SCREEN_HEIGHT: #ant[2] = ROW
		ant[2] = 5
	if ant[2] < 5:
		ant[2] = SCREEN_HEIGHT

	return ant

def modifyColors(ant, matrix):
	cellColor = matrix[ant[2]][ant[1]] #get color of new cell
	if cellColor == 0 or cellColor == 3: #change ant's direction depending on the color of the cell
		ant[0] -= 90
	else:
		ant[0] += 90
	matrix[ant[2]][ant[1]] = (cellColor + 1)%4 #flip the new cell's color in matrix
	newCellColor = matrix[ant[2]][ant[1]] #get new color of cell
	plot(ant[1], ant[2], COLORS[newCellColor]) #display the new cell's color on screen

def makeTheAntsJourney(ant, matrix):
	message = 'PROGRAM CURRENTLY RUNNING ' + str(STEPS) + ' ant moves in ' + str(SPEED_INC) + ' increments.'
	print(message)
	root.title(message)
	startTime = clock()
	for n in range(STEPS):
		move(ant)
		modifyColors(ant, matrix)
		if n % SPEED_INC == 0:
			canvas.update()
	canvas.update()
	displayStatistics(startTime)

SCREEN_WIDTH = 1275
SCREEN_HEIGHT = 685
root = Tk()
canvas = setUpCanvas(root)
ANT_START_ROW = SCREEN_WIDTH//2
ANT_START_COL = SCREEN_HEIGHT//2
STEPS = 20000
SPEED_INC = 20
COLORS = ('WHITE', 'RED', 'BLUE', 'YELLOW', 'GREEN', 'CYAN', 'MAGENTA', 'GRAY', 'PINK')

def main():
	ant, matrix = createPixelWorld()
	makeTheAntsJourney(ant, matrix)
	root.mainloop() #required for graphics

if __name__ == '__main__': main()