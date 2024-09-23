import time, random, copy ,sys

width = 60
height = 20
oldList = []
for x in range(width):
  column = []
  for y in range(height):
    
    if random.randint(0,1) == 0:
      column.append('#')
    else:
      column.append(' ')
  oldList.append(column)

try:
  while True:
    print("\n\n\n\n\n")
    newList = copy.deepcopy(oldList)
    
    for y in range(height):
      for x in range(width):
        print(newList[x][y],end="")
      print()
    
    for x in range(width):
      for y in range(height):
        topCell = (y - 1) % height
        bottomCell = (y + 1) % height
        rightCell = (x + 1) % width
        leftCell = (x - 1) % width
        
        numNeighbors = 0
        if newList[leftCell][topCell] == '#':
          numNeighbors += 1 # Top-left neighbor is alive.
        if newList[x][topCell] == '#':
          numNeighbors += 1 # Top neighbor is alive.
        if newList[rightCell][topCell] == '#':
          numNeighbors += 1 # Top-right neighbor is alive.
        if newList[leftCell][y] == '#':
          numNeighbors += 1 # Left neighbor is alive.
        if newList[rightCell][y] == '#':
          numNeighbors += 1 # Right neighbor is alive.
        if newList[leftCell][bottomCell] == '#':
          numNeighbors += 1 # Bottom-left neighbor is alive.
        if newList[x][bottomCell] == '#':
          numNeighbors += 1 # Bottom neighbor is alive.
        if newList[rightCell][bottomCell] == '#':
          numNeighbors += 1 # Bottom-right neighbor is alive.
        
        if numNeighbors == 3 and newList[x][y] == ' ':
          oldList[x][y] = "#"
        elif newList[x][y] == "#" and (numNeighbors == 2 or
numNeighbors == 3):
          oldList[x][y] = '#'
        else:
          oldList[x][y] = " "
    time.sleep(1)

        
except KeyboardInterrupt:
  sys.exit("You've ended the game")  