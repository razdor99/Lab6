# LEDdisplay class

import time
from shifter import Shifter    # extend by composition

class LEDdisplay():

  'Class for controlling a 7-segment LED display'

  numbers = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]

  def __init__(self, data, latch, clock):
    self.Shifter = Shifter(data, latch, clock)
 
  def setNumber(self, num):  # display a given number
    row = 4 # change this value to pick which row the pattern appears on
    self.Shifter.shiftByte(LEDdisplay.numbers[num]) # load the row values
    self.Shifter.shiftByte(1 << (row-1)) 
    
class LED8x8():
  numbers = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]

  def __init__(self, data, latch, clock):
    self.Shifter = Shifter(data, latch, clock)
  def display(self,row):
    self.Shifter.shiftByte(LEDdisplay.numbers[row]) # load the row values
    self.Shifter.shiftByte(1 << (row-1)) 