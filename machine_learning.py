#Name: Shrey Gupta
#Date: May 2015
#Period: 1

from itertools import permutations
from random import random

def insertX(board, index):
	return(board[:index] + "X" + board[index+1:])

def insertO(board, index):
	return(board[:index] + "O" + board[index+1:])

def stringBoard(perm, limit):
	newBoard = '---------'
	for n in range(limit+1):
		if n%2 == 0: newBoard = insertX(newBoard, perm.index(n))
		else: newBoard = insertO(newBoard, perm.index(n))
	return newBoard

def gameIsWin(board, piece):
	combo = piece*3
	result = False

	#horizontally
	if board[:3] == combo or board[3:6] == combo or board[6:9] == combo:
		result = True

	#vertically
	if board[0] + board[3] + board[6] == combo:
		result = True
	elif board[1] + board[4] + board[7] == combo:
		result = True
	elif board[2] + board[5] + board[8] == combo:
		result = True

	#diagonally
	if board[0] + board[4] + board[8] == combo:
		result = True
	elif board[2] + board[4] + board[6] == combo:
		result = True

	return result

def gameIsTie(board):
	return '-' not in board

def gameOver(board):
	return gameIsWin(board, 'O') or gameIsWin(board, 'X') or gameIsTie(board)

def createDatabase():
	database = set(['---------'])
	sequence = [0, 1, 2, 3, 4, 5, 6, 7, 8]
	filledBoards = list(permutations(sequence, 9))
	for perm in filledBoards:
		for limit in range(8):
			board = stringBoard(perm, limit)
			if not(gameOver(board)):
				database.add(board)
	return database

def writeToTextFile(database):
	f = open('ticTacToeBoards.txt', 'w')
	for board in database:
		f.write(board + "\n")

def makeProbabilities(board):
	probabilities = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	for n in range(len(board)):
		if board[n] == '-':
			probabilities[n] = 7
	return probabilities

def readFromTextFile():
	database = {}
	f = open('ticTacToeBoards.txt', 'r').read().split("\n")
	for line in f:
		database[line] = makeProbabilities(line)
	return database

def makeMove(database, board):
	probabilities = database[board]
	total = sum(probabilities)
	r = random()
	for n in range(len(probabilities)):
		r -= probabilities[n]/(total+0.0000000001)
		if r <= 0: return n
	for n in range(len(probabilities)-1, -1, -1):
		if probabilities[n] != 0: return n

def simulateGame(database):
	movesX = {}; movesO = {}; turn = 0
	board = '---------'
	while not(gameOver(board)):
		if turn%2 == 0:
			index = makeMove(database, board)
			if not(gameOver(board)): movesX[board] = index
			board = insertX(board, index)
		else:
			index = makeMove(database, board)
			if not(gameOver(board)): movesO[board] = index
			board = insertO(board, index)
		turn += 1
	if gameIsWin(board, 'X'):
		for board in movesX: database[board][movesX[board]] += 3
		for board in movesO:
			if database[board][movesO[board]] > 1.1: database[board][movesO[board]] -= 1
			else: database[board][movesO[board]] *= 0.3
	elif gameIsWin(board, 'O'):
		for board in movesX:
			if database[board][movesX[board]] > 1.1: database[board][movesX[board]] -= 1
			else: database[board][movesX[board]] *= 0.3
		for board in movesO: database[board][movesO[board]] += 3
	elif gameIsTie(board):
		for board in movesX: database[board][movesX[board]] += 1
		for board in movesO: database[board][movesO[board]] += 1
	return database

def writeAgainToTextFile(database):
	f = open('boardProbabilities.txt', 'w')
	for board in database:
		f.write(board + ": " + str(database[board]) + "\n")

def readAgainFromTextFile():
	database = {}
	f = open('boardProbabilities.txt', 'r').read().split("\n")
	for line in f:
		temp = line.split(": ")
		database[temp[0]] = eval(temp[1])
	return database

def printBoard(board):
	newBoard = board
	for n in range(len(newBoard)):
		if newBoard[n] == '-': newBoard = newBoard[:n] + str(n) + newBoard[n+1:]
	print("GAME BOARD:")
	for n in range(3):
		print(newBoard[3*n+0] + "\t" + newBoard[3*n+1] + "\t" + newBoard[3*n+2] + "\n")
	for n in range(15): print()

def playGame(database):
	print("Welcome to the game of Tic-Tac-Toe. Human (X) goes first. Good luck!")
	board = '---------'; turn = 0
	while not(gameOver(board)):
		printBoard(board)
		if turn%2 == 0:
			index = int(input("Please make a move: "))
			board = insertX(board, index)
		else:
			index = makeMove(database, board)
			board = insertO(board, index)
		turn += 1
	printBoard(board)
	if gameIsWin(board, 'X'): print("Human (X) WINS. Play again?")
	elif gameIsWin(board, 'O'): print("Computer (O) WINS. Try again next time.")
	elif gameIsTie(board): print("Game is a TIE.")

def main():
	#Part I (Board Creation)
	#database = createDatabase()
	#writeToTextFile(database)

	#Part II (Game Simulations)
	#database = readFromTextFile()
	#for n in range(1000000): database = simulateGame(database)
	#writeAgainToTextFile(database)

	#Part III (Human v. Computer Game)
	database = readAgainFromTextFile()
	playGame(database)

main()