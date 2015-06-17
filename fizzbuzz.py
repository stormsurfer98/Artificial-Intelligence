#################################################
#Name: Shrey Gupta								#
#Date: April 7, 2015							#
#Period: 1 										#
#################################################

for x in range(1, 101):
	if x%3 == 0 and x%5 == 0:
		print("Fizz and Buzz")
	elif x%3 == 0:
		print("Fizz")
	elif x%5 == 0:
		print("Buzz")
	else:
		print(x)

print("It worked")

#Question: Why might a recruiter NOT hire the programmer who could score the higest on a code-puzzle test?
#Reason 1: The program, although it works, may be poorly written and hard to understand/read.
#Reason 2: The program does not contain comments describing what some of the more complicated methods do.
#Reason 3: The programmer might not have good work habits--i.e. come to work late, not do his/her assigned work on time, etc.