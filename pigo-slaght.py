#gopigo autonomous instantiated class
#http://www.dexterindustries.com/GoPiGo/programming/python-programming-for-the-raspberry-pi-gopigo/

from gopigo import *
from turtle import *
import time

#global variable
STOP_DIST = 50

__author__ = 'Spencer'

class Pigo:

    #####
    ##### Basic Status And Methods
    #####

    status = {"ismoving" : False, "servo" : 90, "leftspeed" : 175,
              "rightspeed" : 175, "dist" : 100, "volt" : 2}


    def __init__(self):
        print "as you can see I am a pigo pumpkin"
        self.checkDist()

    def stop(self):
        self.status["ismoving"] = False
        print "holy stop"
        for x in range(3):
            stop()

    def fwd(self):
        self.status["ismoving"] = True
        print "lets a go"
        for x in range(3):
            fwd()

    def bwd(self):
        self.status["ismoving"] = True
        print "back it up please"
        for x in range(3):
            bwd()

# check if conditions are safe to continue opperating
    def keepGoing(self):
        if self.status['dist'] < STOP_DIST:
            print "obstacle detected stopping imediatly"
            return False
        elif volt() > 14 or volt() < 6:
            print "unsafe voltage detected: " + str(volt())
            return False
        else:
            return True

    def checkDist(self):
        self.status['dist'] = us_dist(15)
        print "I see something" + str(self.status['dist']) + "mm away"
        if not self.keepGoing():
            print "emergency stop Ho Lee Fuk"
            self.stop()

    def checkVolt(self):
        self.status['volt'] = volt()
        print "its got voltage over 14!!!!!!!!"

    def circleRight(self):
        print "to the right"
        for x in range(5):
            right_rot()
        time.sleep(1)
        self.stop()


    def circleLeft(self):
        print "To the left"
        for x in range(5):
            left_rot()
        time.sleep(1)
        self.stop()

    def blink(self):
        print "Blinking time!"
        for x in range(5):
            led_on(1)
            time.sleep(.08)
            led_off(1)
        time.sleep(1)
        self.stop()

    def shuffle(self):
        print "twerk"
        for x in range(5):
            left_rot()
            time.sleep(.5)
            right_rot()
            time.sleep(.5)
        time.sleep(1)
        self.stop()


    def servoShake(self):
        print "oh no no no no no"
        for x in range(3):
            servo(135)
            time.sleep(.1)
            servo(45)
        time.sleep(1)
        self.stop()


    #####
    ##### Advanced Status And Methods
    #####

    def safeDrive(self):
        self.fwd()
        while self.keepGoing():
            self.checkDist()
        self.stop()

    def servoSweep(self):
        for ang in range(20, 160, 5):
            servo(ang)
            time.sleep(.1)

    def dance(self):
        self.checkDist()
        print "I just want to dance!"
        if self.keepGoing():
            self.circleRight()
            self.circleLeft()
            self.shuffle()
            self.servoShake()
            self.blink()

#####
##### Main app starts here
#####
ziggypi = Pigo()

ziggypi.dance()

ziggypi.stop()
