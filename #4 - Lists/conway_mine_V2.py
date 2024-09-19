import time, random, copy , sys

nextCell = [] # every inner list is 'x' and every element in the inner list is 'y'
width = 60
height = 20
for x in range(width): #to make sure that you will have 60 inner lists
  column = [] # You will append every 'y' to this list
  for y in range(height): #the inner lists are columns [height]
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
      print()        
    
    for x in range(width):
      for y in range(height):
        topCell = (y - 1) % height
        bottomeCell = (y + 1) % height
        rightCell = (x + 1) % width
        leftCell = (x - 1) % width
        
        neighbors= 0
        if nextCellCopy[rightCell][topCell] == '#':
          neighbors +=1
        if nextCellCopy[rightCell][y] == '#':
          neighbors +=1
        if nextCellCopy[rightCell][bottomeCell] == '#':
          neighbors +=1
        if nextCellCopy[x][bottomeCell] == '#':
          neighbors +=1
        if nextCellCopy[leftCell][bottomeCell] == '#':
          neighbors +=1
        if nextCellCopy[leftCell][y] == '#':
          neighbors +=1
        if nextCellCopy[leftCell][topCell] == '#':
          neighbors +=1
        if nextCellCopy[x][topCell] == '#':
          neighbors +=1
          
        if neighbors == 3:
          nextCell[x][y] = '#'
        elif neighbors == 2 and (neighbors == 3 or neighbors == 2):
          nextCell[x][y] = '#'
        else:
          nextCell[x][y] = ' '     
    time.sleep(1)
except KeyboardInterrupt:
  sys.exit("You've stopped the program")