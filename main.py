import random
import time
import multiprocessing
myArray = multiprocessing.Array('i',8)
while True:
  x = random.randint(1,5)
  row=0
  i=0
  if x == 1:
    #walk up
    if row == 7:
      pass
    else:
      row +=1
    time.sleep(0.1)
  if x == 2:
    #walk down
    if row == 0:
      pass
    else:
      row -=1
    time.sleep(0.1)
  if x == 3:
    #walk left
    myArray[i] = 0
    if i == 0:
      pass
    else:
      i -=1
    myArray[i] = 1
    time.sleep(0.1)

  if x == 4:
    #walk right
    myArray[i] = 0
    if i == 7:
      pass
    else:
      i+=1
    myArray[i] = 1
    time.sleep(0.1)
  print(myArray[:])