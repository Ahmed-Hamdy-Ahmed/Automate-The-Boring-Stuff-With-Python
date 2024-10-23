# I Did it 😉 but I've put the return "" at the end to remove the returned none value
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
# print(column)

  
def printTable(lst):
  maxLen = []
  for i in lst:
    lengths = []
    for j in i:
      lengths.append(len(j))
    maxLen.append(max(lengths))
    
    '''
    the problem in this code is that it just appends the last list which is [['  dogs', '  cats', ' moose', ' goose']]
    '''
  newLst = []
  maxItem = 0
  for i in lst:
    newLstChild = []
    for j in i:
      newLstChild.append(j.rjust(maxLen[maxItem] + 1))
    maxItem += 1
    newLst.append(newLstChild)

    
  row = len(newLst[0])
  num = 0
  lstOrganized = []
  while num != row:
    lstOrganizedchild = []
    for x in range(len(newLst)):
      lstOrganizedchild.append(newLst[x][num])
    num += 1
    lstOrganized.append(lstOrganizedchild)
  
  for i in lstOrganized:
    for j in i:
      print(j , end="")
    print()
  return ""
print(printTable(tableData))
