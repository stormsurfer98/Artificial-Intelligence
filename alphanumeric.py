#Name: Shrey Gupta
#Date: October 20, 2014
#Period: 4

from re import findall
from itertools import permutations

puzzle = 'DOG * CAT == fight'

puzzle = puzzle.upper()
words = findall('[A-Z]+', puzzle)
keys = ''.join(set(''.join(words)))

solutionFound = False
for values in permutations('1234567890', len(keys)):
	table = str.maketrans(keys, ''.join(values))
	equation = puzzle.translate(table)
	try:
		if(eval(equation)):
			print('---', equation)
			solutionFound = True
	except SyntaxError:
		dummy = 0

if(solutionFound):
	print("All solutions have been found.")
else:
	print("No solutions exist.")