#Name: Shrey Gupta
#Date: October 23, 2014
#Period: 4

from math import sqrt
from decimal import Decimal, getcontext
from time import clock

def fib1(n):
	a = 1; b = 1; c = 0
	if(n <= 2):
		return 1
	for x in range(0, n):
		a = b; b = c; c = a + b
	return c

def fib2(n):
	if(n <= 2):
		return 1
	return(fib2(n-1) + fib2(n-2))

def fib3(n):
	a = 1; b = 1
	if(n <= 2):
		return 1
	for x in range(0, n-3):
		a = a + b; b = a - b
	return(a + b)

def fib4(n):
	bases = {1:1, 2:1, 3:2, 4:3, 5:5, 6:8, 7:13, 8:21, 9:34, 10:55}
	if(n <= 10):
		return bases[n]
	return(fib4(n-1) + fib4(n-2))

def fib5(n):
	return {1:1, 2:1, 3:2, 4:3, 5:5, 6:8, 7:13, 8:21, 9:34, 10:55, 11:89, 12:144}[n]

def fib6(n, bases = {1:1, 2:1}):
	if(not(n in bases)):
		bases[n] = (fib6(n-1, bases) + fib6(n-2, bases))
	return(bases[n])

def fib7(n):
	phi = (1+sqrt(5))/2
	phi2 = -1/phi
	return(round((pow(phi, n) - pow(phi2, n))/sqrt(5)))

def fib8(n):
	if(n > 70):
		getcontext().prec = 2*n
	phi = (Decimal(1) + Decimal(5).sqrt())/Decimal(2)
	phi2 = (Decimal(1) - Decimal(5).sqrt())/Decimal(2)
	return(round((pow(Decimal(phi), Decimal(n)) - pow(Decimal(phi2), Decimal(n)))/Decimal(5).sqrt()))

def main():
	start = clock() #No. 1
	print("1.", fib1(39))
	print("Time:", round(clock()-start, 1), "seconds\n")

	start = clock() #No. 2
	print("2.", fib2(39))
	print("Time:", round(clock()-start, 1), "seconds\n")

	start = clock() #No. 3
	print("3.", fib3(39))
	print("Time:", round(clock()-start, 1), "seconds\n")

	start = clock() #No. 4
	print("4.", fib4(39))
	print("Time:", round(clock()-start, 1), "seconds\n")

	start = clock() #No. 5
	print("5.", fib5(12))
	print("Time:", round(clock()-start, 1), "seconds\n")

	start = clock() #No. 6
	print("6.", fib6(39))
	print("Time:", round(clock()-start, 1), "seconds\n")

	start = clock() #No. 7
	print("7.", fib7(39))
	print("Time:", round(clock()-start, 1), "seconds\n")

	start = clock() #No. 8
	print("8.", fib8(39))
	print("Time:", round(clock()-start, 1), "seconds")

main()