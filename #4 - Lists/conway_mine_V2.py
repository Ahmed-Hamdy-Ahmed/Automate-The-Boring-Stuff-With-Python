#I didn't end this version yet
import time, random, copy , sys

nextCell = [] # every inner list is 'x' and every element in the inner list is 'y'
width = 60
height = 20
for x in range(width): #to make sure that you will have 60 inner lists
  for y in range(height): #the inner lists are columns [height]
    column = [] # You will append every 'y' to this list
    if random.randint(0, 1) == 0:
      column.append('#')
    else:
      column.append(' ')
  nextCell.append(column)
try:
  while True:
    print('\n\n\n\n')
    nextCellCopy = copy.deepcopy(nextCell)
    for y in range(height):
      for x in range(width):
        print(nextCellCopy[x][y] , end="")
    
        
    
    
except KeyboardInterrupt:
  sys.exit("You've stopped the program")