#Name: Shrey Gupta
#Date: December 18, 2014
#Period: 4

from random import randint

countG = 0; countS = 0
drawer = (('G', 'G'), ('G', 'S'), ('S', 'S'))
for x in range(0, 100000):
	coin1 = ''; coin2 = ''
	while coin1 != 'G':
		r1 = randint(0, 1); r2 = randint(0, 1)
		coin1 = drawer[r1][r2]
	if r2 == 0: coin2 = drawer[r1][1]
	else: coin2 = drawer[r1][0]
	if coin2 == 'G': countG += 1
	else: countS += 1

print("Probability:", str(round(countG/1000, 2))+"%", "\n")