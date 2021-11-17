# LEDdisplay class

import multiprocessing, time
from shifter import Shifter    # extend by composition
import random

class LEDdisplay():

  'Class for controlling a 7-segment LED display'

  #numbers = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]

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
    column = 0b00000001
    self.Shifter = Shifter(data, latch, clock)
    row = 5
    i = 5
    
    while True:
      x = random.randint(1,5)
      if x == 1:
        #walk up
        row +=1

        
      if x == 2:
        #walk dowm
        row -=1
        
      if x == 3:
        #walk left
        i -=1
        f = column << 1
       
      if x == 4:
        #walk right
        i+=1
        f = column >> 1
        

      if x == 5:
        #stay still
        pass
        
    myArray[i]=f
    p1 = multiprocessing.Process(target=self.display, args=(myArray,row))
    p1.daemon = True
    p1.start()
    time.sleep(0.1)
    
       
  def display(self,row):
    self.Shifter.shiftByte(LED8x8.pattern[row]) # load the row values
    self.Shifter.shiftByte(1 << (row))
    self.Shifter.latch()