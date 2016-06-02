# Solution to the counting sheep puzzle from google code jam qualification round 2016 
# pass command line parameters of input file name and output file name
# By Zack Akil 25/05/2016 

import sys

# problem logic

def sheepCount(value):
   if(value == 0):
    return 'INSOMNIA'
   numList = '0123456789'
   i = 0
   current = 0
   while(len(numList)!=0): # whilst numList has chars in it
    i += 1
    current = i * value
    convert = str(current)
    for x in xrange(len(numList)-1,-1,-1): # for each remaining char in numList
      if(numList[x]in convert):
        numList = numList.replace(numList[x],'') # remove char from numList
   return current

#  file reading/writing logic

if len(sys.argv) >=3:
  inputFile = sys.argv[1]
  outputFile = sys.argv[2]
else:
  inputFile = input('Enter input file name: ')
  outputFile = input('Enter output file name: ')

f = open(inputFile, 'r')
rows = int(f.readline())

w = open(outputFile, 'w')
for x in xrange(0,rows):
  w.write('Case #{}: {}'.format(x+1, sheepCount(int(f.readline().rstrip()))))
  if x < rows - 1:
     w.write('\n')