#Name: Shrey Gupta
#Date: April 7, 2015
#Period: 1

def printMatrix(text, matrix):
	print("---", text, ":", sep = "")
	for r in range(len(matrix)):
		for c in range(len(matrix[0])):
			print(round(matrix[r][c], 2), "\t\t", end = "")
		print()
	print()

def multiplyMatrix(matrix1, matrix2):
	newMatrix = [0]*len(matrix2[0])
	for x in range(len(matrix2[0])):
		for y in range(len(matrix1[0])):
			newMatrix[x] += (matrix1[0][y]*matrix2[y][x])
	return [newMatrix]

def main():
	m1 = [[1.123, 1.456, 1.799], [22.123, 22.456111, 22.799], [30.123, 300.456, 3000.799999]]
	m2 = [[1, 3, 6, 10]]
	m3 = [[3, 2, 1], [4, 5, 6], [3, 6, 9], [2, 4, 6]]
	printMatrix("MATRIX M1", m1)
	printMatrix("MATRIX M2", m2)
	printMatrix("MATRIX M3", m3)
	newMatrix = multiplyMatrix(m2, m3)
	printMatrix("MATRIX M2 * M3", newMatrix)

main()