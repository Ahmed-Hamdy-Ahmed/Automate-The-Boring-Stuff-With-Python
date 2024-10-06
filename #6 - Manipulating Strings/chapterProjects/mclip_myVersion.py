#! python3
# this is a mini clipboard program
import sys, pyperclip

phrases = {
  'hello': 'Hello , How is it going!',
  'busy': 'Sorry, but can we do it next week',
  'free': 'I will met you today.'
}

if len(sys.argv) < 2:
  print('Syntax: py mclip.py [keyphrase] - copy phrase text')
else:
  userArg = sys.argv[1]

  if userArg in phrases:
    pyperclip.copy(phrases[userArg])
    print(f'The response for {userArg} has been coppied')
  else:
    print(f'There\'s no response for {userArg}')