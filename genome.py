#Name: Shrey Gupta
#Date: March 2015
#Period: 4

from random import randint

def createPopulation(size):
	population = []
	for n in range(size):
		creature = []
		for i in range(10): creature.append(randint(0, 1))
		population.append(creature)
	return population

def fitness(creature):
	return sum(creature)

def mateTwoCreatures(parent1, parent2):
	split = randint(1, 9)
	child1 = parent1[:split] + parent2[split:]
	child2 = parent2[:split] + parent1[split:]
	return [child1, child2]

def matePopulation(population):
	population = sorted(population, key=lambda creature: fitness(creature), reverse=True)
	newPopulation = []
	for creature in range(1, 6):
		newPopulation += mateTwoCreatures(population[0], population[creature])
	return newPopulation

def printPopulation(roundNumber, population):
	print("--- ROUND:", roundNumber, "---")
	for creature in population:
		print(creature)
	print()

def main():
	population = createPopulation(12) #increase size to increase 1's
	printPopulation("INITIAL POPULATION", population)
	for n in range(1, 11):
		population = matePopulation(population)
		printPopulation(n, population)

main()