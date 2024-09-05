import sys
def collatz(number):
      if number % 2 == 0:
        return number // 2
      elif number % 2 == 1:
        return 3 * number + 1
while True:
  try:
    userInput = int(input("Choose a number:\n"))
    collatzSeq = collatz(userInput)
    if collatzSeq == 1:
      sys.exit(f'The output is {collatzSeq}')
    else:
      print(f'The output is {collatzSeq}')
  except ValueError:
    print("You must type a number ,try again!")