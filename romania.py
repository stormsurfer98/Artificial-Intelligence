#Name: Shrey Gupta
#Period: 4
#Date: September 25, 2014

import pickle
import sys
import math

myFile = open("stationhash.txt", "rb")
d = pickle.load(myFile)
myFile.close()

myFile = open("stationlist.txt", "rb")
stationList = pickle.load(myFile)
myFile.close()

myFile = open("stationcoordinates.txt", "rb")
stationCoor = pickle.load(myFile)
myFile.close()

station1 = input("Please enter a station: ")
station1 = station1[0]
station2 = input("Please enter another station: ")
station2 = station2[0]

if(not(station1 in d)):
   sys.exit(station1 + " does not exist in the dictionary.")
if(not(station2 in d)):
   sys.exit(station2 + " does not exist in the dictionary.")

def calc(y1, x1, y2, x2):
  x1 = float(x1)
  y1 = float(y1)
  x2 = float(x2)
  y2 = float(y2)
  R = 3958.76 #miles
  x1 *= (math.pi)/180.0
  y1 *= (math.pi)/180.0
  x2 *= (math.pi)/180.0
  y2 *= (math.pi)/180.0
  return math.acos(math.sin(y1)*math.sin(y2)+math.cos(y1)*math.cos(y2)*math.cos(x2-x1))*R

queue = [(0, station1, [], 0)]
closed = {}
count = 0

while(queue): #f = element[0], node = element[1], path = element[2], g = element[3]
  element = queue.pop(0)
  count += 1
  if(element[1] == station2):
    element[2].append(station2)
    print("Path:", element[2])
    print("Pops:", count)
    print("Distance:", element[3])
    break
  else:
    closed[element[1]] = element[3]
    children = d[element[1]]
    for c in children:
      g = calc(stationCoor[element[1]][0], stationCoor[element[1]][1], stationCoor[c][0], stationCoor[c][1])
      h = calc(stationCoor[c][0], stationCoor[c][1], stationCoor[station2][0], stationCoor[station2][1])
      if(c in closed):
        if(closed[c] > element[3] + g):
          del closed[c]
          path = list(element[2])
          path.append(element[1])
          queue.append((element[3]+g+h, c, path, element[3]+g))
      else:
        b = True
        for q in queue:
          if(c in q):
            if(q[3] > element[3] + g):
              queue.remove(q)
              path = list(element[2])
              path.append(element[1])
              queue.append((element[3]+g+h, c, path, element[3]+g))
            b = False
        if(b):
          path = list(element[2])
          path.append(element[1])
          queue.append((element[3]+g+h, c, path, element[3]+g))
  queue.sort()