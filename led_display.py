# LEDdisplay class

import multiprocessing, time
from shifter import Shifter    # extend by composition
import random

class LEDdisplay():

  'Class for controlling a 7-segment LED display'

  def __init__(self, data, latch, clock):
    self.Shifter = Shifter(data, latch, clock)
 
  def setNumber(self, num):  # display a given number
    row = 4 # change this value to pick which row the pattern appears on
    self.Shifter.shiftByte(LEDdisplay.numbers[num]) # load the row values
    self.Shifter.shiftByte(1 << (row-1)) 
    
class LED8x8():
  
  def __init__(self, data, latch, clock):
    myArray = multiprocessing.Array('i',8)
    #myArray[0], myArray[1],myArray[2],myArray[3],myArray[4],myArray[5],myArray[6],myArray[7],= 0b10000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000
    mask = 0b11111111
    column = 0b00000001
    self.Shifter = Shifter(data, latch, clock)
    row = 5
    i = 5
    
    while True:
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
        if i ==7:
          pass
          #walk left
        else:
          i -=1
          column = column << 1
       
      if x == 4:
        #walk right
        if i ==0:
          pass
        else:
          i+=1
          column = column >> 1
        

      if x == 5:
        #stay still
        pass
        
      myArray[row] = ~column & mask
      self.p1 = multiprocessing.Process(target=self.display, args=(myArray,row))
      self.p1.daemon = True
      self.p1.start()
      time.sleep(0.1)
    
       
  def display(self,a,row):

    self.Shifter.shiftByte(a[row]) # load the row values
    self.Shifter.shiftByte(1 << int(row))
    self.Shifter.latch()
