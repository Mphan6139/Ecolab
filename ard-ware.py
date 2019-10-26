import pyfirmata
import time

board = pyfirmata.Arduino('/dev/cu.usbmodem14101')
LED_BUILTIN = 13

while True:
    board.digital[LED_BUILTIN].write(1)
    time.sleep(1)
    board.digital[LED_BUILTIN].write(0)
    time.sleep(1)
