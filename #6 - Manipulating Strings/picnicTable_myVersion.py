def printPicnic(itemsDict, leftJust, rightJust):
  print('PICNIC ITEMS'.center(rightJust + leftJust, "-"))
  for k, v in itemsDict.items():
    print(k.ljust(leftJust, '.') + str(v).rjust(rightJust))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)