#Name: Shrey Gupta
#Period: 4
#Date: September 16, 2014

import pickle
import sys

word1 = input("Please enter a six letter word: ")
word2 = input("Please enter another six letter word: ")

f = open("wordhash.txt", "rb")
d = pickle.load(f)
f.close()

if(not(word1 in d)):
   sys.exit(word1 + " does not exist in the dictionary.")
if(not(word2 in d)):
   sys.exit(word2 + " does not exist in the dictionary.")

for key in d:
  d[key] = [d[key], -1, -1]

usedWords = [word1]
d[word1][1] = 0
d[word1][2] = "None"

queue = [word1]
count = 0

while(queue):
  element = queue.pop(0)
  count += 1
  if(element == word2):
    break
  neighbors = d[element][0]
  level = d[element][1]
  for n in neighbors:
    if(not(n in usedWords)):
      queue.append(n)
      d[n] = [d[n][0], level+1, element]
      usedWords.append(n)

element2 = word2
myList = []
while(True):
  if(d[element2][2] == "None"):
    myList.append(element2)
    break
  myList.append(element2)
  element2 = d[element2][2]
  
myList.reverse()
print(myList)
print(count)