# I didn't finish this project 
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
# print(column)

# maxLen = []
# for i in tableData:
#   lengths = []
#   for j in i:
#     lengths.append(len(j))
#   maxLen.append(max(lengths))
  
def printTable(lst):
  row = len(lst[0])
  num = 0
  lstOrganized = []
  while num != row:
    for x in range(len(lst)):
        lstOrganized.append(lst[x][num])
    num += 1
  return lstOrganized
print(printTable(tableData))