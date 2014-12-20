#Name: Shrey Gupta
#Period: 4

import math

f = open("words.txt")
a = []
for line in f:
  a.append(line.rstrip("\n"))

word = input("Please enter a six letter word: ")

for w in a:
  count = 0
  for x in range(0, 6):
    if(word[x] != w[x]):
      count += 1
  if(count == 1):
    print(w)