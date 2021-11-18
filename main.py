import random
row =5
i=5
column = 0b00000001
mask=0b00000000
for t in range(50):
  x = random.randint(1,5)
  if x == 1:
    if row == 7:
      pass
    else:
      row +=1
      #walk up
    
  if x == 2:
    if row == 0:
      pass
    else:
      #walk down
      row -=1
    
  if x == 3:
    if i ==0:
      pass
      #walk left
    else:
      i -=1
      column = column << 1
    
  if x == 4:
    #walk right
    if i ==7:
      pass
    else:
      i+=1
      column = column >> 1
    

  if x == 5:
    #stay still
    pass
  print(bin(column & ~mask))
  print(row)