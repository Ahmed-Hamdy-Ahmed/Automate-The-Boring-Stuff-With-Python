#I made this program to check if I understand the topic
import pyperclip
lastCopy = ''
copyContent = [] 
while True:
  try:
    newCopy = pyperclip.paste()
    if newCopy != lastCopy:
      copyContent.append(newCopy)
    lastCopy = newCopy
  except KeyboardInterrupt:
    for item in copyContent:
      print(item)