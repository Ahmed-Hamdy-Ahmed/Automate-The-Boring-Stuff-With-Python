while True:
    print("Who are you?")
    name = input()
    if name != 'joe':
        continue
    print("Hello , Joe. What is the password? (it is a fish.)")
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
