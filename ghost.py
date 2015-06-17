#Name: Shrey Gupta
#Date: December 2014
#Period: 4

import random

class Node(object):
	def __init__(self, value):
		self.value = value
		self.children = {}

	def __repr__(self):
		self.print()
		return ''

	def print(self, stng=''):
		if not(self.children):
			print('-->', stng[1:])
		else:
			stng += self.value
			for key in self.children:
				self.children[key].print(stng)

	def display(self):
		if self.value == '$': return
		print('\n--- NODE ---')
		print('--> self.value =', self.value)
		print('--> self.children: [', end = '')
		for key in self.children:
			if key != '$':
				print(key, sep = '', end = ', ')
		print(']')
		print('--- END ---')
		for char in self.children:
			(self.children[char]).display()

	def insert(self, stng):
		stng = stng.lower()
		if stng == '':
			self.children['$'] = Node('$')
		else:
			while not(stng[0].isalpha()):
				stng = stng[1:]
			if stng[0] in self.children:
				self.children[stng[0]].insert(stng[1:])
			elif stng[0] not in self.children.keys():
				p = Node(stng[0])
				self.children[p.value] = p
				p.insert(stng[1:])

	def search(self, stng):
		if stng == '':
			if '$' in self.children:
				return True
			else:
				return False
		if stng[0] in self.children:
			return self.children[stng[0]].search(stng[1:])
		return False

	def randomChild(self):
		r = random.choice(list(self.children))
		while r == '$':
			r = random.choice(list(self.children))
		return r

	def searchForNextLetter(self, stng):
		if stng == '':
			return self.randomChild()
		if stng[0] in self.children:
			return self.children[stng[0]].searchForNextLetter(stng[1:])
		return stng

	def fragmentInDictionary(self, stng):
		if stng == '':
			return True
		if stng[0] in self.children:
			return self.children[stng[0]].fragmentInDictionary(stng[1:])
		return False

def createTrieFromDictionaryFile():
	root = Node('*')
	f = open('ghostDictionary.txt', 'r')
	for line in f:
		root.insert(line.strip())
	return root

def formatString(stng):
	stng = stng.upper()
	formattedString = ''
	for char in stng:
		formattedString += (char + '-')
	return formattedString

def spellWordFromString(root, stng):
	finalStng = stng + root.searchForNextLetter(stng)
	while not(root.search(finalStng)):
		finalStng += root.searchForNextLetter(finalStng)
	return finalStng

def requestAndCheckHumanMove(root, stng):
	stng += (input('HUMAN: ' + formatString(stng))[0]).lower()
	if root.search(stng) and len(stng) > 3:
		print('--- GAME OVER: HUMAN LOSES because "', formatString(stng)[0:-1], '" is a word.', sep='')
		print()
		exit()
	if root.fragmentInDictionary(stng) == False:
		print('--- GAME OVER: HUMAN LOSES because "', formatString(stng)[0:-1], '" does not begin any word. The', sep='')
		print("computer's word was ", '"', formatString(spellWordFromString(root, stng[0:-1]))[0:-1], '".', sep='')
		print()
		exit()
	return(stng)

def requestAndCheckComputerMove(root, stng):
	stng += root.searchForNextLetter(stng)
	print('COMPUTER:', formatString(stng)[0:-1])
	if root.search(stng) and len(stng) > 3:
		print('--- GAME OVER: COMPUTER LOSES because "', formatString(stng)[0:-1], '" is a word.', sep='')
		print()
		exit()
	return(stng)

def main():
	root = createTrieFromDictionaryFile()
	print('Welcome to the game of GHOST! The human goes first. Enter your letters in the')
	print('pop-up dialog boxes. Good luck!')
	stng = ''
	while True:
		stng = requestAndCheckHumanMove(root, stng)
		stng = requestAndCheckComputerMove(root, stng)

if __name__ == '__main__':
	main()