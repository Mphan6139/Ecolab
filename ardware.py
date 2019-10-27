import pyfirmata
import asyncio
import time
from classifier import *
from landing import *

board = pyfirmata.Arduino('/dev/cu.usbmodem14101')
buttonPin = 2
PinDict = {'y':13, 'r': 12, 'b': 11}

buttonState = 0
lightOn = False

## button code
it = pyfirmata.util.Iterator(board)
it.start()

board.digital[buttonPin].mode = pyfirmata.INPUT

def place_holder():
    #ArdWare.light('y', 1)
    return 1
resulty = lambda x: 'b'
class ArdWare:
    def __init__(self,funky = place_holder, gunky = None):
        self.lightOn = False
        self.funky = funky
        if not gunky:
            self.gunky = resulty
        else:
            self.gunky = gunky
        self.loopy()
    def loopy(self):
        while True:
            self.sw = board.digital[buttonPin].read()
            if not self.sw: # button has been pressed
                self.light('y',1)
                self.buttonPressed()
            time.sleep(0.1)

    def light(self,color,on_or_off):
        board.digital[PinDict[color]].write(on_or_off)
    def buttonPressed(self):
        r1 = self.funky()
        r2 = self.gunky(r1)
        self.final_light(r2)

    def final_light(self, b_or_r):
        self.light('y', 0)
        self.light(b_or_r, 1) # turn light on
        time.sleep(0.1)
        self.light(b_or_r, 0)
        self.loopy()


## testing
a = ArdWare(take_picture, get_user)
