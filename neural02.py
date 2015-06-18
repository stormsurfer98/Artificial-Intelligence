#Name: Shrey Gupta
#Date: May/June 2015
#Period: 1

from random import random, choice

TRIALS = 3000
ALPHA = 0.25
SMALL = 0.4
INPUTS = [(0, 0, -1, 0), (0, 1, -1, 1), (1, 0, -1, 1), (1, 1, -1, 0)]

def f(w, x):
	return int((w[0]*x[0] + w[1]*x[1] + w[2]*x[2]) > 0)

def trained(w):
	for vector in INPUTS:
		if f(w, vector) != vector[3]:
			return False
	return True

def verifyNetwork(w, epochs):
	print("Epochs =", epochs)
	print("Trained =", trained(w))
	print("List of inputs/outputs:")
	for vector in INPUTS:
		print("Input =", vector, "\t", "Output =", f(w, vector))

def initializeWeights():
	return [random(), random(), random()]

def trainPerceptronsWeights():
	epochs = 0
	w = initializeWeights()
	while epochs < TRIALS and not(trained(w)):
		x = choice(INPUTS)
		y = f(w, x); t = x[3]
		w[0] = w[0] - ALPHA*(y-t)*x[0]
		w[1] = w[1] - ALPHA*(y-t)*x[1]
		w[2] = w[2] - ALPHA*(y-t)*x[2]
		epochs += 1
	return w, epochs

def main():
	w, epochs = trainPerceptronsWeights()
	verifyNetwork(w, epochs)

if __name__ == '__main__': main()