#Name: Shrey Gupta
#Date: April 2015
#Period: 1

from tkinter import Tk, Canvas, YES, BOTH
from operator import itemgetter
from itertools import permutations
from copy import deepcopy
from random import shuffle
from time import clock
from math import hypot

def setUpCanvas(root):
    root.title("THE TRAVELING SALESMAN PROBLEM by Shrey Gupta")
    canvas = Canvas(root, width  = root.winfo_screenwidth(), height = root.winfo_screenheight(), bg = 'black')
    canvas.pack(expand = YES, fill = BOTH)
    return canvas

def script(x, y, msg = '', kolor = 'WHITE'):
    canvas.create_text(x, y, text = msg, fill = kolor,  font = ('Helvetica', 10, 'bold'))

def plot(city):
    x = city[1]+5; y = city[2]+5
    if city[0] == -1:
        kolor = 'WHITE'
    else: kolor = 'YELLOW'
    canvas.create_rectangle(x-2, y-2, x+2, y+2, width = 1, fill = kolor)

def line(city1, city2, kolor = 'RED'):
    canvas.create_line(city1[1]+5, city1[2]+5, city2[1]+5, city2[2]+5, width = 1, fill = kolor)

def displayDataInConsole(AlgorithmResults, baseCity, city):
    print('===<Traveling Salesman Path Statistics>===')
    print ('   algorithm         path length ')
    for element in AlgorithmResults:
    	print ('---%-20s'%element[0], int(element[2]))
    city.sort()
    baseCity.sort()
    if city == baseCity:
        print("---Data verified as unchanged.")
    else:
        print ('ERROR: City data has been corrupted!')
    print('   Run time =', round(clock()-START_TIME, 2), ' seconds.')

def printCity(city):
    count = 0
    for (id,x,y) in city:
        print( '%3d: id =%2d, (%5d, %5d)'%(count,id, int(x), int(y)))
        count += 1

def displayPathOnScreen(city, statistics):
    (minX, maxX, minY, maxY, meanX, meanY, medianX, medianY, size, m, b) = statistics
    canvas.delete('all')
    cityNorm, (p,q,r,s) = normalizeCityDataToFitScreen(city[:], statistics)

    cityNorm.append(cityNorm[0])
    plot(cityNorm[0])
    for n in range(1, len(cityNorm)):
        plot(cityNorm[n])
        line(cityNorm[n], cityNorm[n-1])
    script(650,  20, 'path length = ' + str(pathLength(city)))
    canvas.create_rectangle(530,10, 770, 30, width = 1, outline = 'WHITE')
    canvas.update()
    root.mainloop()

def normalizeCityDataToFitScreen(city, statistics):
    (minX, maxX, minY, maxY, meanX, meanY, medianX, medianY, size, m, b) = statistics
    newCity = []

    for (id, x,y) in city:
        newCity.append ( (id, x-minX, y-minY))

    (x0,y0) = (maxX-minX, m*maxX+b - minY)
    (x1,y1) = (minX-minX, m*minX+b - minY)

    maxX = maxX-minX
    maxY = maxY-minY

    cityNorm = []
    for (id, x, y) in newCity:
        cityNorm.append ((id, x*SCREEN_WIDTH/maxX, y*SCREEN_HEIGHT/maxY))

    (x0,y0) = x0/maxX*SCREEN_WIDTH, y0/maxY*SCREEN_HEIGHT
    (x1,y1) = x1/maxX*SCREEN_WIDTH, y1/maxY*SCREEN_HEIGHT

    return cityNorm, (x1,y1,x0,y0)

def readDataFromFileAndAppendId(fileName):
    file1 = open(fileName, 'r')
    fileLength = int(file1.readline())
    city = []
    for elt in range(fileLength):
       x, y = file1.readline().split()
       city.append([0, float(x), float(y)])
    file1.close()
    return city

def pathLength(city):
    totalPath = 0
    for n in range(1, len(city)):
        totalPath += dist( city[n-1], city[n] )
    totalPath += dist( city[n], city[0] )
    return int(totalPath)

def dataStatistics(city):
    xValues = []
    yValues = []
    size = len(city)
    for (id, x,y) in city:
        xValues.append(x)
        yValues.append(y)
    minX = min(xValues)
    maxX = max(xValues)
    minY = min(yValues)
    maxY = max(yValues)

    assert (minX >= 0 or maxX >= 0 or minY >= 0 or maxY >= 0)

    meanX = sum(xValues)/size
    meanY = sum(yValues)/size
    medianX = city[len(city)//2][0]
    medianY = city[len(city)//2][1]

    xyDiff   = 0
    xDiffSqr = 0
    for (id, x,y) in city:
        xyDiff  += (meanX - x)*(meanY - y)
        xDiffSqr+= (meanX - x)**2

    m = xyDiff/xDiffSqr
    b = meanY - m*meanX

    return minX, maxX, minY, maxY, meanX, meanY, medianX, medianY, size, m, b

def dist(cityA, cityB):
    return hypot(cityA[1]-cityB[1], cityA[2] - cityB[2])

root = Tk()
canvas = setUpCanvas(root)
START_TIME = clock()
SCREEN_WIDTH = root.winfo_screenwidth()//5*5 - 15
SCREEN_HEIGHT = root.winfo_screenheight()//5*5 - 90
fileName = "salesman.txt"

def main():
    city  = readDataFromFileAndAppendId(fileName)
    statistics = (minX, maxX, minY, maxY, meanX, meanY, medianX, medianY, size, m, b) = dataStatistics(city)
    shuffle(city)
	#sort on y-coordinate and connect sequentially by y.
	#sort on x-coordinate and connect sequentially by x.
	#other algorithms
    displayPathOnScreen(city, statistics)

if __name__ == '__main__': main()