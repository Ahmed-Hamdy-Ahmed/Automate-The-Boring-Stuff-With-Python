def addToInventory(inventory, addedItems):
  print("Inventory:")
  totalItems =0
  for item in addedItems:
    inventory.setdefault(item, 0)
    inventory[item] +=1
  print(inventory)
  for k,v in inventory.items():
    totalItems += v
  return f"Total number of items: {totalItems}"

stuff = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
print(addToInventory(stuff, dragonLoot))
