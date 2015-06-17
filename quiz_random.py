#Name: Shrey Gupta
#Date: 11/13/14
#Period: 4

from random import choice, random, randrange, shuffle, sample

#No. 1
print("1.", choice([-1, 1]))

#No. 2
if(random() < .5): print("2.", -1)
else: print("2.", 1)

#No. 3
print("3.", randrange(-1, 2, 2))

#No. 4
seq = [-1, 1]
shuffle(seq)
print("4.", seq[0])

#No. 5
seq = [-1, 1]
print("5.", sample(seq, 1)[0])