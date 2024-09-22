import random
numberOfStreaks = 0
for experimentNumber in range(10000):
  # Code that creates a list of 100 'heads' or 'tails' values.
  hOrT= []
  for i in range(100):
    if random.randint(0,1) == 0:
      hOrT.append('T')
    else:
      hOrT.append('H')
  
  # Code that checks if there is a streak of 6 heads or tails in a row.
  streak = 0
  for x in range(len(hOrT)):
    if hOrT[x] == hOrT[x - 1]:
      streak += 1
    else:
      streak = 0
    if streak == 6:
      streak = 1
      numberOfStreaks +=1
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
print(numberOfStreaks)