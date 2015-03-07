#Problem: The Letter Shift Function (Interview Quiz 2)
#Name: Shrey Gupta
#Date: February 9, 2015
#Period: 1

def lettershift(word, shift):
	new_word = ""
	for char in word:
		if char.isalpha():
			if char.isupper():
				new_word += chr((ord(char)+shift-65)%26+65)
			else: #if char is lowercase
				new_word += chr((ord(char)+shift-97)%26+97)
		else: #if char is not a letter
			new_word += char
	return new_word

def main():
	word = input("Enter a word: ")
	shift = input("Enter a number n: ")
	if word != "" and shift != "":
		print("Shifted word:", lettershift(word, int(shift)))
	else:
		print("Please enter a valid input!")

main()