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
  pattern = [0b10000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000, 0b00000000]

  def __init__(self, data, latch, clock):
    self.Shifter = Shifter(data, latch, clock)
    myArray = multiprocessing.Array('i',8) #is it 5 bc of positions or 8 bc of bits
    row = 0 
    i = 0
    
    while True:
      x = random.randint(1,5)
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

      if x == 5:
        #stay still
        pass
        time.sleep(0.1)

    p1 = multiprocessing.Process(target=LED8x8.display, args=(myArray,row))
    p1.daemon = True
    p1.start()
    
       
  def display(self,row):
    self.Shifter.shiftByte(LED8x8.pattern[row]) # load the row values
    self.Shifter.shiftByte(1 << (row))
    self.Shifter.latch()