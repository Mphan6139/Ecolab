import pyfirmata
import threading
import time
# from daemon import Daemon
from classifier import *
from landing import *
from multiprocessing import Process
PIDFILE = '/var/run/yourdaemon.pid'

# board = pyfirmata.Arduino('/dev/cu.usbmodem14101')
board = pyfirmata.Arduino('COM3')
buttonDict = {0:2, 1: 5}
PinDict = {'y':13, 'r': 12, 'b': 11}

buttonState = 0
lightOn = False

## button code
it = pyfirmata.util.Iterator(board)
it.start()

board.digital[buttonDict[0]].mode = pyfirmata.INPUT
board.digital[buttonDict[1]].mode = pyfirmata.INPUT


def place_holder():
    #ArdWare.light('y', 1)
    return 1
resulty = lambda x: 'b'
class ArdWare():
    def __init__(self):
        self.lightOn = False
        self.first_run = True
        # self.funky = funky
        # if not gunky:
        #     self.gunky = resulty
        # else:
        #     self.gunky = gunky
        # self.t = threading.Thread(target = self.loopy, daemon = True)
        # self.t.setDaemon(True)
        # self.t.start()
        # io.run(self.loopy())
        # with daemon.DaemonContext():
        #     self.loopy()
        #t.join()
        # Daemon.__init__(self,PIDFILE)
        # print('hi')

    def run(self):
        while True:
            self.bp1 = board.digital[buttonDict[0]].read()
            self.bp2 = board.digital[buttonDict[1]].read()
            if not self.bp1 and not self.first_run: # button 0 has been pressed
                # print(self.bp1, self.first_run)
                self.light('y',1)
                self.buttonPressed(0)

            elif not self.bp2 and not self.first_run:

                self.light('y',1)
                self.buttonPressed(1)
            time.sleep(0.1)
            self.first_run = False


    def light(self,color,on_or_off):
        board.digital[PinDict[color]].write(on_or_off)

    def buttonPressed(self,user_num):

        user = get_user(user_num)
        r1 = take_picture()
        # r2 = user.process_result(r1)
        r2 = True
        if r2:
            self.final_light('b')
        else:
            self.final_light('r')

    def final_light(self, b_or_r):

        self.light('y', 0)
        self.light(b_or_r, 1) # turn light on
        time.sleep(5)
        self.light(b_or_r, 0)
        # self.t = threading.Thread(target = self.loopy)
        # self.t.setDaemon(True)
        # self.t.start()
        # self.run()


## testing
# d = ArdWare()
# d.start()
d = ArdWare()
p = Process(target=d.run)
