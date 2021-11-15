#Shifter class

import RPi.GPIO as GPIO
import time
from led_display import LEDdisplay
class Shifter():

  'Shift register class'

  def __init__(self, data, latch, clock):
    self.dataPin, self.latchPin, self.clockPin = data, latch, clock
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.dataPin, GPIO.OUT) 
    GPIO.setup(self.latchPin, GPIO.OUT, initial=0)
    GPIO.setup(self.clockPin, GPIO.OUT, initial=0)

  def ping(self, pin):  # ping the clock or latch pin
    GPIO.output(pin,1)
    time.sleep(0)
    GPIO.output(pin,0)

  def shiftByte(self, byteVal):  # display a given byte pattern
    for i in range(8):           # 8 bits in register
      #GPIO.output(self.dataPin, ~(byteVal & (1<<i)))  # if common anode
      GPIO.output(self.dataPin, byteVal & (1<<i))    # if common cathode
      self.ping(self.clockPin)
    self.ping(self.latchPin)

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