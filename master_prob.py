#############################################################
# Name: Shrey Gupta											#
# Date: February 12, 2015									#
# Period: 1 												#
#############################################################

from random import random, uniform

def determineProbability(side1, side2, side3):
	minSide = min(side1, side2, side3)
	maxSide = max(side1, side2, side3)
	mySet = [side1, side2, side3]
	mySet.remove(minSide); mySet.remove(maxSide)
	mediumSide = mySet.pop()

	if(minSide + mediumSide > maxSide):
		return(True)
	return(False)

def puzzle1(k):
	count = 0.0
	for n in range(0, k):
		r1 = random(); r2 = random()

		side1 = abs(r2 - r1)
		side2 = min(r1, r2)
		side3 = 1 - max(r1, r2)

		if determineProbability(side1, side2, side3):
			count += 1

	return count/k

def puzzle2(k):
	count = 0.0
	for n in range(0, k):
		r1 = random()
		side1 = uniform(r1, 1-r1)

		r2 = uniform(side1, 1)
		side2 = min(r2-side1, 1-r2)
		side3 = max(r2-side1, 1-r2)

		if determineProbability(side1, side2, side3):
			count += 1

	return count/k

def puzzle3(k):
	count = 0.0
	for n in range(0, k):
		r1 = random()
		if(random() < .5): side1 = r1
		else: side1 = 1-r1

		r2 = uniform(side1, 1)
		side2 = min(r2-side1, 1-r2)
		side3 = max(r2-side1, 1-r2)

		if determineProbability(side1, side2, side3):
			count += 1

	return count/k

def puzzle4(k):
	count = 0.0
	for n in range(0, k):
		r1 = random()
		if(random() < r1): side1 = 1-r1
		else: side1 = r1

		r2 = uniform(side1, 1)
		side2 = min(r2-side1, 1-r2)
		side3 = max(r2-side1, 1-r2)

		if determineProbability(side1, side2, side3):
			count += 1

	return count/k

def main(k):
	print("Puzzle 1 answer:", puzzle1(k))
	print("Puzzle 2 answer:", puzzle2(k))
	print("Puzzle 3 answer:", puzzle3(k))
	print("Puzzle 4 answer:", puzzle4(k))

main(10000000)