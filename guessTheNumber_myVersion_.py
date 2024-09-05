import random
print('I am thinking of a number between 1 and 20.')
randNum = random.randint(1,20)
i = 1
while True:
    guessNum = int(input('Take a guess.'))
    if guessNum > randNum:
        print('Your guess is too high.')
    elif guessNum < randNum:
        print('Your guess is too low.')
    else:
        print(f'Good job! You guessed my number in {i} guesses!')
        break
    i +=1



