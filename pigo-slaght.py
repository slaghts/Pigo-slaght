from gopigo import *
import time

#global variable
STOP_DIST = 50

__author__ = 'Spencer'

class Pigo:

    #####
    ##### Basic Status And Methods
    #####

    status = {"ismoving" : False, "servo" : 90, "leftspeed" : 175,
              "rightspeed" : 175, "dist" : 100}


    def __init__(self):
        print "as you can see I am a pigo pumpkin"
        self.checkDist()

    def stop(self):
        self.isMoving = false
        print "holy shit"
        for x in range(3):
            stop()

    def fwd(self):
        self.["ismoving"] = True
        print "lets a go"
        for x in range(3):
            fwd()

    def bwd(self):
        self.["ismoving"] = True
        print "back it up please"
        for x in range(3):
            bwd()

    def keepGoing(self):
        if self.status['dist'] < STOP_DIST:
            return False
        else
            return True

    def checkDist():
        self.status['dist'] = us_dist(15)
            print "I see something" + str(self.status['dist']) + "mm away"

    #####
    ##### Advanced Status And Methods
    #####

    def dance(self):
        self.status['dist'] = us_dist(15)
        print "I just want to dance!"
        if self.keepGoing():
            self.circleRight()
            self.circleLeft()
            self.suffle()
            self.servoShake()
            self.blink()

#####
##### Main app starts here
#####
Moto = Pigo()
while Moto.keepGoing():
    Moto.fwd()
    Time.sleep(2)
    Moto.stop()

Moto.stop()
