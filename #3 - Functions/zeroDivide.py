print("The output of the first function")
def spamOne(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spamOne(2))
print(spamOne(12))
print(spamOne(0))
print(spamOne(1) , "\n")

print("The output of the second function")
def spamTwo(divideBy):
  return 42 / divideBy

try:
  print(spamTwo(2))
  print(spamTwo(12))
  print(spamTwo(0))
  print(spamTwo(1))
except ZeroDivisionError:
  print('Error: Invalid argument.')