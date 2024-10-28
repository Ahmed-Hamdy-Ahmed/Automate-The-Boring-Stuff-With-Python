import random

messages = ['It is certain',
    'It is decidedly so',
    'Yes definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

# if you removed the "-1" it may return index error
#because the 2nd number in randint is included
print(messages[random.randint(0, len(messages) - 1)])