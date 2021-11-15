# LEDdisplay class

import time
from shifter import Shifter    # extend by composition

class LEDdisplay():

  'Class for controlling a 7-segment LED display'

  numbers = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]

  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)
 
  def setNumber(self, num):  # display a given number
    row = 4 # change this value to pick which row the pattern appears on
    self.shifter.shiftByte(LEDdisplay.numbers[num]) # load the row values
    self.shifter.shiftByte(1 << (row-1)) 
    
class LED8x8():
  def __init__(self):
    self.self = self
  def display(self):
    global num
    for x in range(7):
      for i in range(2):
        row = x # change this value to pick which row the pattern appears on
        self.shifter.shiftByte(LEDdisplay.numbers[num]) # load the row values
        self.shifter.shiftByte(1 << (row-1)) 