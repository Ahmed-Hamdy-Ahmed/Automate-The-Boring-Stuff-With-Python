#English to Pig latin translator
message = input("Type your message please:\t")
vowels = ('a', 'e', 'i', 'o', 'u', 'y')

pigLat= []
for word in message.split():
  
  preifixNonLetter= ''
  while len(word) > 0 and not word[0].isalpha():
    preifixNonLetter += word[0]
    word = word[1:]
  if len(word) == 0:
    pigLat.append(preifixNonLetter)
    continue
  
  suffixNonLetter = ''
  while not word[-1].isalpha():
    suffixNonLetter += word[-1]
    word = word[:-1]
    
  wasUpper = word.isupper()
  wasTitle = word.istitle()
  word = word.lower()
  
  consonant = ''
  while word[0] not in vowels:
    consonant += word[0]
    word= word[1:]
    
  if consonant == '':
    word += 'yay'
  else:
    word += consonant + 'ay'
  
  if wasUpper:
    word = word.upper()
  elif wasTitle:
    word = word.title()
  
  pigLat.append(preifixNonLetter + word + suffixNonLetter)

print(' '.join(pigLat))