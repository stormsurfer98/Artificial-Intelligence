#Name: Shrey Gupta
#Date: March 2015
#Period: 1

from tkinter import Tk, Canvas, YES, BOTH

WIDTH = 1275 #root.winfo_screenwidth()
HEIGHT = 685 #root.winfo_screenheight()
FSIZE = 2 #font size of chr(9607) = solid block

def setUpCanvas(root):
	root.title("WOLFRAM'S CELLULAR AUTOMATA by Shrey Gupta")
	canvas = Canvas(root, width = WIDTH, height = HEIGHT, bg = 'BLACK')
	canvas.pack(expand = YES, fill = BOTH)
	return canvas

def printList(rule):
	#print the title
	canvas.create_text(170, 20, text = "Rule: " + str(rule), fill = 'gold', font = ('Helvetica', 10, 'bold'))

	#set up list (L) and print the top row
	L = [1]
	canvas.create_text(637, 50, text = chr(9607), fill = 'RED', font = ('Helvetica', FSIZE, 'bold'))

	#print one line per iteration
	for row in range(1, 256):
		L = [0, 0] + L + [0, 0]; newL = []
		for n in range(0, len(L) - 2):
			bin = str(L[n]) + str(L[n+1]) + str(L[n+2])
			newL.append(rule[int(bin, 2)])
		L = newL
		for n in range(0, len(L)):
			if L[n] == 0: kolor = 'BLACK'
			else: kolor = 'RED'
			canvas.create_text(637 - row*FSIZE + n*FSIZE, row*FSIZE + 50, text = chr(9607), fill = kolor, font = ('Helvetica', FSIZE, 'bold'))

root = Tk()
canvas = setUpCanvas(root)

def main():
	#rule = [0, 0, 0, 1, 1, 1, 1, 0] #rule 30 = strange
	rule = [0, 1, 0, 1, 1, 0, 1, 0] #rule 90 = pretty picture
	#rule = [0, 1, 1, 0, 1, 1, 1, 0] #rule 110 = half strange
	#rule = [1, 1, 0, 0, 1, 1, 1, 0] #rule 206 = semi-solid triangle
	#rule = [1, 1, 1, 1, 1, 1, 1, 1] #rule 255 = solid triangle
	printList(rule)
	root.mainloop() #required for graphics

if __name__ == '__main__': main()