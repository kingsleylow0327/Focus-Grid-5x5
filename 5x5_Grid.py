#Starting the Program
import random
llist = ["{:02d}".format(i) for i in range(1, 26)]
random.shuffle(llist)

final = []
for i in range(5):
  mini = llist[i*5:5+i*5]
  print(mini)
  final.append(mini)

