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

def h(word1, word2):
  return sum([word1[x] != word2[x] for x in range(0, 6)])

queue = [(h(word1, word2), word1, [], 0)]
closed = {}
count = 0

while(queue):
  element = queue.pop(0)
  count += 1
  if(element[1] == word2):
    element[2].append(word2)
    print(element[2])
    print(count)
    break
  else:
    closed[element[1]] = element[3]
    children = d[element[1]]
    for c in children:
      if(c in closed):
        if(closed[c] > element[3] + 1):
          del closed[c]
          path = list(element[2])
          path.append(element[1])
          queue.append((element[3]+1+h(c, word2), c, path, element[3]+1))
      else:
        b = True
        for q in queue:
          if(c in q):
            if(q[3] > element[3] + 1):
              queue.remove(q)
              path = list(element[2])
              path.append(element[1])
              queue.append((element[3]+1+h(c, word2), c, path, element[3]+1))
            b = False
        if(b):
          path = list(element[2])
          path.append(element[1])
          queue.append((element[3]+1+h(c, word2), c, path, element[3]+1))
  queue.sort()