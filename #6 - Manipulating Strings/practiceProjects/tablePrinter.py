# I Did it 😉 and I've put the return "" at the end to remove the returned none value
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
  
def printTable(lst):
  #this block checks the longest string in the list
  maxLen = []
  for i in lst:
    lengths = []
    for j in i:
      lengths.append(len(j))
    maxLen.append(max(lengths))
    
  #this code right justifies every inner list
  newLst = []
  maxItem = 0
  for i in lst:
    newLstChild = []
    for j in i:
      newLstChild.append(j.rjust(maxLen[maxItem] + 1))
    maxItem += 1
    newLst.append(newLstChild)
  print(newLst)
  print()
  #this code organize lists to rows instead of columns
  row = len(newLst[0])
  num = 0
  lstOrganized = []
  while num != row:
    lstOrganizedchild = []
    for x in range(len(newLst)):
      lstOrganizedchild.append(newLst[x][num])
    num += 1
    lstOrganized.append(lstOrganizedchild)

  #this code prints the innerlist as a table without returning none value
  for i in lstOrganized:
    for j in i:
      print(j , end="")
    print()
  return ""
print(printTable(tableData))
