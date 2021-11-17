
from led_display import LED8x8
import multiprocessing, time

# Simple demonstration of the LEDdisplay class.
# Note that we don't need RPi.GPIO here since all the I/O
# is done through the LEDdisplay class (we do however need
# to define the GPIO pins, since LEDdisplay is
# pin-agnostic).

dataPin, latchPin, clockPin = 23, 24, 25
L=LED8x8(dataPin, latchPin, clockPin)
# Pick a number sequence
#sequence = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 0b10100101, 0b10011001, 0b01000010, 0b00111100]

#theLEDdisplay= LED8x8(dataPin, latchPin, clockPin)
#myArray = multiprocessing.Array('f',3)
#p1 = multiprocessing.Process(target=theLEDdisplay.display, args=(myArray))



    
