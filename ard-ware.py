import pyfirmata
import asyncio

board = pyfirmata.Arduino('/dev/cu.usbmodem14101')
buttonPin = 2
PinDict = {'y':13, 'r': 12, 'b': 11}

buttonState = 0
lightOn = False

## button code
it = pyfirmata.util.Iterator(board)
it.start()

board.digital[buttonPin].mode = pyfirmata.INPUT

# while True:
#     sw = board.digital[buttonPin].read()
#     if sw is False and not lightOn:
#         lightOn = True
#         board.digital[ledPinYellow].write(1)
#         time.sleep(3)
#         lightOn = False
#     elif lightOn:
#         board.digital[ledPinYellow].write(1)
#     else:
#         board.digital[ledPinYellow].write(0)
#         time.sleep(0.1)
# while True:
#     sw = board.digital[buttonPin].read()
#     #if sw is False:
#         ## send message to backend

class ArdWare:
    def __init__(self,condition = None):
        self.lightOn = True
        self.condition = condition
        self.loopy()
    def loopy(self):
        while True:
            self.sw = board.digital[buttonPin].read()
            if not self.sw and not self.lightOn:
                self.lightOn = True
                self.light('y',1)
                time.sleep(3)
                self.lightOn = False
            elif self.lightOn:
                self.light('y',1)
            else:
                self.light('y',1)
            time.sleep(0.1)

    async def light(self,color,on_or_off):
        board.digital[PinDict[color]].write(on_or_off)
    async def buttonPressed(self):
        return self.sw

## testing
a = ArdWare()
a.light('b',1)






# while True:
#     board.digital[LED_BUILTIN].write(1)
#     time.sleep(1)
#     board.digital[LED_BUILTIN].write(0)
#     time.sleep(1)
