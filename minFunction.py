#Name: Shrey Gupta
#Date: April 2015
#Period: 4

from random import random
from math import sin

def main():
	minValue = 9223372036854775807
	for n in range(10000):
		x = random()*10; y = random()*10
		f = x*sin(4*x) + 1.1*y*sin(2*y)
		if f < minValue: minValue = f
	print("MIN VALUE:", minValue)

main()