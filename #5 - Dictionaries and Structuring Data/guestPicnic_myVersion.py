allGuests = { 'Alice': {'apples': 5, 'pretzels': 12}, 
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1} }
def itemsBrought(guests, item):
  totalBrought = 0
  for k,v in guests.items():
    totalBrought += v.get(item, 0)
  return totalBrought

print(f"Yo've {str(itemsBrought(allGuests, "apple"))} Apples")
print(f"Yo've {str(itemsBrought(allGuests, "banana"))} Banana")
print(f"Yo've {str(itemsBrought(allGuests, "apple pies"))} Apple pies")
print(f"Yo've {str(itemsBrought(allGuests, "cups"))} cups")

