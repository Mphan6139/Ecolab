mport pyfirmata
import time

board = pyfirmata.Arduino('/dev/cu.usbmodem14101')
buttonPin = 2
ledPinYellow = 13
ledPinRed = 12
ledPinBlue = 11

buttonState = 0
lightOn = False

## button code
it = pyfirmata.util.Iterator(board)
it.start()

board.digital[buttonPin].mode = pyfirmata.INPUT

while True:
    sw = board.digital[buttonPin].read()
    if sw is False and not lightOn:
        lightOn = True
        board.digital[ledPinYellow].write(1)
        time.sleep(3)
        lightOn = False
    elif lightOn:
        board.digital[ledPinYellow].write(1)
    else:
        board.digital[ledPinYellow].write(0)
        time.sleep(0.1)
while True:
    sw = board.digital[buttonPin].read()
    #if sw is False:
        ## send message to backend
# while True:
#     board.digital[LED_BUILTIN].write(1)
#     time.sleep(1)
#     board.digital[LED_BUILTIN].write(0)
#     time.sleep(1)
