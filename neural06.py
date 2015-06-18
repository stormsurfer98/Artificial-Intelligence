#Name: Shrey Gupta
#Date: May/June 2015
#Period: 1

from random import random, choice, shuffle

TRIALS = 3000000
ALPHA = 0.25
SMALL = 0.4
INPUTS = [(0.01, 2, -1, 0, 0), (2, 0.01, -1, 0, 0), (-0.01, 2, -1, 0, 1), (-2, 0.01, -1, 0, 1), 
		  (-2, -0.01, -1, 1, 1), (-0.01, -2, -1, 1, 1), (0.01, -2, -1, 1, 0), (2, -0.01, -1, 1, 0)]
TEST = INPUTS + [(1, 1, -1, 0, 0), (-1, 1, -1, 0, 1), (-1, -1, -1, 1, 1), (1, -1, -1, 1, 0)]
shuffle(INPUTS); shuffle(TEST)

def f(w, x):
	return [int((w[0][0]*x[0] + w[1][0]*x[1] + w[2][0]*x[2]) > 0),
			int((w[0][1]*x[0] + w[1][1]*x[1] + w[2][1]*x[2]) > 0)]

def trained(w):
	for vector in INPUTS:
		if f(w, vector) != [vector[3], vector[4]]:
			return False
	return True

def verifyNetwork(w, epochs):
	print("Epochs =", epochs)
	print("Trained =", trained(w))
	print("Line separators: ", "y = ", round(w[0][0]/w[1][0], 2), "x + ", round(w[2][0]/w[1][0], 2), 
		  " and y = ", round(w[0][1]/w[1][1], 2), "x + ", round(w[2][1]/w[1][1], 2), sep = "")
	print("List of inputs/outputs:")
	for vector in TEST:
		print("Input =", vector, "       \t", "Output =", f(w, vector))

def initializeWeights():
	return [(random(), random()), (random(), random()), (random(), random())]

def trainPerceptronsWeights():
	epochs = 0
	w = initializeWeights()
	while epochs < TRIALS and not(trained(w)):
		x = choice(INPUTS)
		y = f(w, x); t = [x[3], x[4]]
		w[0] = [w[0][0] - ALPHA*(y[0]-t[0])*x[0], w[0][1] - ALPHA*(y[1]-t[1])*x[0]]
		w[1] = [w[1][0] - ALPHA*(y[0]-t[0])*x[1], w[1][1] - ALPHA*(y[1]-t[1])*x[1]]
		w[2] = [w[2][0] - ALPHA*(y[0]-t[0])*x[2], w[2][1] - ALPHA*(y[1]-t[1])*x[2]]
		epochs += 1
	return w, epochs

def main():
	w, epochs = trainPerceptronsWeights()
	verifyNetwork(w, epochs)

if __name__ == '__main__': main()