#I made this version after looking at the author's code
import sys ,random

print("ROCK, PAPER, SCISSORS")

wins = 0
losses = 0
ties = 0

while True:
  print(f'{wins} Wins, {losses} Losses, {ties} Ties')
  while True:
    playerMove = input('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    if playerMove == 'q':
      sys.exit()
    if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
      break
    print("Type one of r , p ,s or q")
  
  if playerMove == 'r':
    print("Rock versus...")
  elif playerMove == 'p':
    print("Paper versus...")
  else:
    print("Scissors versus...")
    
  randomNumber =random.randint(1,3)
  if randomNumber == 1:
    computerMove = 'r'
    print("Rock")
  elif randomNumber == 2:
    computerMove = 'p'
    print("paper")
  else:
    computerMove = "s"
    print("Scissors")
  
  if playerMove == computerMove:
    ties += 1
  elif playerMove == 'r' and computerMove == 's':
    wins += 1
  elif playerMove == 'r' and computerMove == 'p':
    losses += 1
  elif playerMove == 's' and computerMove == 'r':
    losses += 1
  elif playerMove == 's' and computerMove == 'p':
    wins += 1
  elif playerMove == 'p' and computerMove == 's':
    losses += 1
  elif playerMove == 'p' and computerMove == 'r':
    wins += 1  
