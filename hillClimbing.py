#Name: Shrey Gupta
#Date: April 2015
#Period: 4

from random import random
from math import sin, cos, pi, sqrt
import time

def f(x, y):
	if x <= 0 or x >= 10 or y <= 0 or y >= 10:
		return float("inf")
	return x*sin(4*x) + 1.1*y*sin(2*y)

def randomSearch(count):
	minValue = 9223372036854775807
	minX = -1; minY = -1
	for n in range(count):
		x = random()*10; y = random()*10
		valueF = f(x, y)
		if valueF < minValue:
			minValue = valueF
			minX = x; minY = y
	print("MIN VALUE:", minValue)
	print("(X, Y): (", minX, ", ", minY, ")", sep="")

def frange(start, stop, step):
	i = start
	while i < stop:
		yield i
		i += step

def hillClimbing(count, radius):
	minF = 9223372036854775807
	minX = -1; minY = -1
	for n in range(count):
		x = random()*10; y = random()*10
		while(True):
			trialMinX = x; trialMinY = y
			trialMinF = f(trialMinX, trialMinY)
			for t in frange(0, 2*pi, 2*pi/64):
				trialX = x + radius*cos(t)
				trialY = y + radius*sin(t)
				trialF = f(trialX, trialY)
				if trialF < trialMinF:
					trialMinF = trialF
					trialMinX = trialX; trialMinY = trialY
			if(x == trialMinX and y == trialMinY):
				break
			x = trialMinX; y = trialMinY
		if(f(x, y) < minF):
			minF = f(x, y)
			minX = x; minY = y
	print("MIN VALUE:", minF)
	print("(X, Y): (", minX, ", ", minY, ")", sep="")

def hillClimbingWithTable(count, radius):
	sinTable = {}; cosTable = {}
	minF = 9223372036854775807
	minX = -1; minY = -1
	for n in range(count):
		x = random()*10; y = random()*10
		while(True):
			trialMinX = x; trialMinY = y
			trialMinF = f(trialMinX, trialMinY)
			for t in frange(0, 2*pi, 2*pi/64):
				if t not in sinTable: sinTable[t] = sin(t)
				if t not in cosTable: cosTable[t] = cos(t)
				trialX = x + radius*cosTable[t]
				trialY = y + radius*sinTable[t]
				trialF = f(trialX, trialY)
				if trialF < trialMinF:
					trialMinF = trialF
					trialMinX = trialX; trialMinY = trialY
			if(x == trialMinX and y == trialMinY):
				break
			x = trialMinX; y = trialMinY
		if(f(x, y) < minF):
			minF = f(x, y)
			minX = x; minY = y
	print("MIN VALUE:", minF)
	print("(X, Y): (", minX, ", ", minY, ")", sep="")

def generator(n):
	for x in range(n):
		yield x

def hillClimbingWithGrid(length, width, radius):
	minF = 9223372036854775807
	minX = -1; minY = -1
	for i in generator(length):
		for j in generator(width):
			x = i; y = j
			while(True):
				trialMinX = x; trialMinY = y
				trialMinF = f(trialMinX, trialMinY)
				for t in frange(0, 2*pi, 2*pi/64):
					trialX = x + radius*cos(t)
					trialY = y + radius*sin(t)
					trialF = f(trialX, trialY)
					if trialF < trialMinF:
						trialMinF = trialF
						trialMinX = trialX; trialMinY = trialY
				if(x == trialMinX and y == trialMinY):
					break
				x = trialMinX; y = trialMinY
			if(f(x, y) < minF):
				minF = f(x, y)
				minX = x; minY = y
	print("MIN VALUE:", minF)
	print("(X, Y): (", minX, ", ", minY, ")", sep="")

def addVectors(*vectors):
	newVector = [0, 0]
	for v in vectors:
		newVector[0] += v[0]
		newVector[1] += v[1]
	return newVector

def multiplyVector(v, c):
	return [c*x for x in v]

def nelderMead(count):
	minF = 9223372036854775807
	minX = -1; minY = -1
	for n in range(count):
		vectors = [[random()*10, random()*10], [random()*10, random()*10], [random()*10, random()*10]]
		vectors = sorted(vectors, key=lambda v: f(v[0], v[1]), reverse = True)
		a = vectors[0]; b = vectors[2]; c = vectors[1]
		for j in range(20):
			m = multiplyVector(addVectors(b, c), 0.5)
			d = addVectors(b, c, multiplyVector(a, -1))
			if f(d[0], d[1]) < f(a[0], a[1]):
				e = multiplyVector(addVectors(multiplyVector(b, 3), multiplyVector(c, 3), multiplyVector(a, -4)), 0.5)
				if f(e[0], e[1]) < f(d[0], d[1]): a = e
				else: a = d
			else:
				h = multiplyVector(addVectors(multiplyVector(b, 3), multiplyVector(c, 3), multiplyVector(a, -2)), 0.25)
				g = multiplyVector(addVectors(multiplyVector(a, 2), b, c), 0.25)
				if f(h[0], h[1]) < f(a[0], a[1]) or f(g[0], g[1]) < f(a[0], a[1]):
					if f(h[0], h[1]) < f(g[0], g[1]): a = h
					else: a = g
				else:
					vectors = [multiplyVector(addVectors(a, b), 0.5), multiplyVector(addVectors(c, b), 0.5), b]
					vectors = sorted(vectors, key=lambda v: f(v[0], v[1]), reverse = True)
					a = vectors[0]; b = vectors[2]; c = vectors[1]
		if(f(a[0], a[1]) < minF):
			minF = f(a[0], a[1])
			minX = a[0]; minY = a[1]
	print("MIN VALUE:", minF)
	print("(X, Y): (", minX, ", ", minY, ")", sep="")

def main():
	start_time = time.time()
	print("\n--- RANDOM SEARCH:")
	randomSearch(10000)
	print("RUN TIME: %s seconds\n" % round(time.time()-start_time, 5))

	start_time = time.time()
	print("--- HILL-CLIMBING:")
	hillClimbing(100, 0.1)
	print("RUN TIME: %s seconds\n" % round(time.time()-start_time, 5))

	start_time = time.time()
	print("--- HILL-CLIMBING WITH LOOK-UP TABLE:")
	hillClimbingWithTable(100, 0.1)
	print("RUN TIME: %s seconds\n" % round(time.time()-start_time, 5))

	start_time = time.time()
	print("--- HILL-CLIMBING WITH GRID:")
	hillClimbingWithGrid(10, 10, 0.1)
	print("RUN TIME: %s seconds\n" % round(time.time()-start_time, 5))

	start_time = time.time()
	print("--- NELDER-MEAD ALGORITHM:")
	nelderMead(250)
	print("RUN TIME: %s seconds\n" % round(time.time()-start_time, 5))

main()