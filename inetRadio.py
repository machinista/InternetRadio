#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import subprocess
import thread
import threading

'''
# GPIO pin-outs:

GPIO-05 - Terminal A 
GPIO-06 - Terminal B
GPIO-12 - Terminal C
GPIO-13 - Terminal D
'''

class MpcControl:

    def __init__(self):
        pass
    
    def mpcPlay(self, channel):
        status = subprocess.check_output(["mpc", "play", channel], stdin=None, stderr=None, shell=False, universal_newlines=False)

    def mpcStop(self):
        status = subprocess.check_output(["mpc", "stop"], stdin=None, stderr=None, shell=False, universal_newlines=False)
                
    def mpcStatus(self):
        status = subprocess.check_output(["mpc", "status"], stdin=None, stderr=None, shell=False, universal_newlines=False)
        print status
    
def main():
    
    #GPIO.setmode(GPIO.BCM)
    #gpioId = [5, 6, 12, 13];
    #gpioState = [];
    #gpioNum = len(gpioId)
                       
    # GPIO reading code - ignore for now
    
    #GPIO set up as inputs. All pulled up
    #for i in range(gpioNum):
        #GPIO.setup(gpioId[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
   
    #for i in range(gpioNum):
        #switch = switch + str(GPIO.input(gpioId[i]))
    #print switch
    
    def playerControl():
        print "runnning in a thread"
        switch = ""
        userCmd = MpcControl()
    
        while True:
        
            print "Commands"
            print "1: Play channel 1"
            print "2: Play channel 2"
            print "3: Stop player"
            print "4: Display player status"
            userSelect = raw_input("Enter command: ")
            
            if (switch == '0111') or (userSelect == '1'):
                userCmd.mpcPlay("1")
    
            elif (switch == '1011') or (userSelect == '2'):
                userCmd.mpcPlay("2")
    
            elif userSelect == '3':
                userCmd.mpcStop()
    
            elif userSelect == '4':
                userCmd.mpcStatus()
    
    def generateChannel():
        a = 0111
        b = 1011
        while True:
            c = a
            time.sleep(10)
            print c
            return c
    
    def threadTest(threadName, delay):
        while True:
            time.sleep(delay)
            print "Hello from thread " + threadName + "\n"
    
    #thread.start_new_thread(generateChannel())
    #thread.start_new_thread(playerControl,(1))


    #while True:
    #    playerControl()
            
if __name__ == '__main__':
    main()
