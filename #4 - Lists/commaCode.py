spam = ['apples', 'bananas', 'tofu', 'cats']

def comma(list):
  listStr = ""
  if len(list) == 0:
    return "The list is empty"
  for str in list:
    if str == list[-2]:
      listStr += str + " and "
    elif str == list[-1]:
      listStr += str
    else:
      listStr += str + ", "
  return listStr
print(comma(spam))
    