#Name: Shrey Gupta
#Date: December 4, 2014
#Period: 4

def reverseLst(Lst):
	L = len(Lst)
	return [Lst[n] for n in range(L-1, -1, -1)]
#-------------------------------------------------------------------------------------------------------------------------------------------------------

def main():
#---Method 1. Use the built-in reverse function.
	Lst1 = [1, 2, 3, 4, 5,]
	Lst2 = list(Lst1)
	Lst2.reverse()
	print('Method 1.', Lst1, Lst2) #Output: Method 1. [1, 2, 3, 4, 5] [5, 4, 3, 2, 1]
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#---Method 2. Use the built-in reversed function.
	Lst1 = [1, 2, 3, 4, 5,]
	Lst2 = list(reversed(Lst1))
	print('Method 2.', Lst1, Lst2)
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#---Method 3. Use slicing only--no loops.
	Lst1 = [1, 2, 3, 4, 5,]
	Lst2 = Lst1[::-1]
	print('Method 3.', Lst1, Lst2)
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#---Method 4. Use a for loop that works on this swap principle: a, b = b, a.
	Lst1 = [1, 2, 3, 4, 5,]
	L = len(Lst1)
	Lst2 = list(Lst1)
	for n in range(0, L//2):
		Lst2[n], Lst2[L-n-1] = Lst2[L-n-1], Lst2[n]
	print('Method 4.', Lst1, Lst2)
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#---Method 5. Use a for loop (not a comprehension) that runs backward and copies each Lst1 element to Lst2.
	Lst1 = [1, 2, 3, 4, 5,]
	Lst2 = []
	for n in range(L-1, -1, -1):
		Lst2.append(Lst1[n])
	print('Method 5.', Lst1, Lst2)
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#---Method 6. Use a list comprehension that runs backward and copies each Lst1 element to Lst2.
	Lst1 = [1, 2, 3, 4, 5,]
	L = len(Lst1)
	Lst2 = [Lst1[n] for n in range(L-1, -1, -1)]
	print('Method 6.', Lst1, Lst2)
#-------------------------------------------------------------------------------------------------------------------------------------------------------

#---Method 7. This time, place method 6 in a function. Anticipate what you can be criticized for, even if your function works perfectly.
	Lst1 = [1, 2, 3, 4, 5,]
	Lst2 = reverseLst(Lst1)
	print('Method 7.', Lst1, Lst2)

main()