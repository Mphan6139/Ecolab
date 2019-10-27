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
    def __init__(self):
        self.lightOn = False
        self.first_run = True
        # self.funky = funky
        # if not gunky:
        #     self.gunky = resulty
        # else:
        #     self.gunky = gunky
        self.loopy()
    def loopy(self):
        while True:
            self.sw = board.digital[buttonPin].read()
            if not self.sw and not self.first_run: # button has been pressed
                self.light('y',1)
                self.buttonPressed(0)
                return
            time.sleep(0.1)
            self.first_run = False


    def light(self,color,on_or_off):
        board.digital[PinDict[color]].write(on_or_off)
    def buttonPressed(self,user_num):
        user = get_user(user_num)
        r1 = take_picture()
        r2 = user.process_result(r1)
        if r2:
            self.final_light('b')
        else:
            self.final_light('r')


    def final_light(self, b_or_r):
        self.light('y', 0)
        self.light(b_or_r, 1) # turn light on
        time.sleep(5)
        self.light(b_or_r, 0)
        self.loopy()


## testing

a = ArdWare()
