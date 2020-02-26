#Starting the Program
import random
llist = ["{:02d}".format(i) for i in range(1, 26)]
random.shuffle(llist)

final = []
for i in range(5):
  mini = llist[i*5:5+i*5]
  print(mini)
  final.append(mini)

iCurrent = 0

for i in range(25):
  iRow, iCol = input().split()
  iRow, iCol = int(iRow), int(iCol)
  if (iRow > 5 or iCol >5):
    print("Exceed Grid Limit")
    break
  if (int(final[iRow-1][iCol-1]) == iCurrent+1):
    iCurrent += 1
    continue
  else:
    break

print("Your result is", iCurrent)