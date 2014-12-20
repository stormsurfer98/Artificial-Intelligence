#Name: Shrey Gupta
#Date: December 2014
#Period: 4

from sys import setrecursionlimit; setrecursionlimit(100)
from time import clock

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

def main():
	root = Node('*')
	root.insert('cat')
	root.insert('catnip')
	root.insert('cats')
	root.insert('catnap')
	root.insert("can't")
	root.insert('cat-x')
	root.insert('dog')
	root.insert('dogs')
	root.insert('dognip')
	print('--- PRINT ---')
	root.print('')
	print('--- END ---')
	root.display()
	print('SEARCH:', root.search('junk'))
	printElapsedTime()

def printElapsedTime():
	print('\nTotal run time =', round(clock() - startTime, 2), 'seconds.')

if __name__ == '__main__': startTime = clock(); main()