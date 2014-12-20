#Name: Shrey Gupta
#Period: 4
#Date: September 25, 2014

import pickle

def putFileIntoArray():
   myFile = open("romNodes.txt")
   stationList, stationCoor = {}, {}
   for line in myFile:
      parts = line.split()
      stationList[parts[0]] = ""
      stationCoor[parts[0]] = [float(parts[1]), float(parts[2])]
   myFile = open("romFullNames.txt")
   for line in myFile:
      stationList[line[0]] = line.strip()
   return stationList, stationCoor

def createDictionary(stationList):
   dictionary = {}
   for str in stationList:
      dictionary[str] = []
   myFile = open("romEdges.txt")
   for line in myFile:
      parts = line.split()
      dictionary[parts[0]].append(parts[1])
      dictionary[parts[1]].append(parts[0])
   return dictionary
      
def putIntoFile(element, fileName):
   myFile = open(fileName, "wb")
   pickle.dump(element, myFile)
   myFile.close()

def main():
   stationList, stationCoor = putFileIntoArray()
   dictionary = createDictionary(stationList)
   putIntoFile(stationList, "stationlist.txt")
   putIntoFile(dictionary, "stationhash.txt")
   putIntoFile(stationCoor, "stationcoordinates.txt")
   print("Done!")
   
main()