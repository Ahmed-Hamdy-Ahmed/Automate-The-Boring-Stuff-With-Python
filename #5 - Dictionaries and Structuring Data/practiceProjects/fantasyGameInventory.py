def displayInventroy(inventory):
  print("Inventory:")
  totalItems = 0
  for k, v in inventory.items():
    print(v,k)
    totalItems += v
  print("Total number of items: " + str(totalItems))
    
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

displayInventroy(stuff)