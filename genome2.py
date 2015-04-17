#Name: Shrey Gupta
#Date: April 2015
#Period: 4

from random import randint
from math import sin

def createPopulation(size, genes):
	population = [[str(randint(0, 1)) for c in range(genes)] for r in range(size)]
	return population

def fitness(creature):
	x = int(''.join(creature[0:10]), 2)/102.3
	y = int(''.join(creature[10:20]), 2)/102.3
	return(x*sin(4*x) + 1.1*y*sin(2*y))

def mateTwoCreatures(parent1, parent2):
	split = randint(1, 19)
	child1 = parent1[:split] + parent2[split:]
	child2 = parent2[:split] + parent1[split:]
	return [child1, child2]

def matePopulation(population):
	population = sorted(population, key=lambda creature: fitness(creature))
	newPopulation = []
	for creature in range(1, len(population)//2 + 1):
		newPopulation += mateTwoCreatures(population[0], population[creature])
	return newPopulation

def printPopulation(roundNumber, population):
	print("--- ROUND:", roundNumber, "---")
	print("FITNESS:", fitness(population[0]))
	print()

def main():
	population = createPopulation(200, 20)
	printPopulation("INITIAL POPULATION", population)
	for n in range(1, 6):
		population = matePopulation(population)
		printPopulation(n, population)

main()