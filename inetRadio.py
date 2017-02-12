#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import subprocess

'''
# GPIO pin-outs:

GPIO-05 - Terminal A 
GPIO-06 - Terminal B
GPIO-12 - Terminal C
GPIO-13 - Terminal D
'''

class MpcCmd(object):

    def __init__(self):
        pass
    
    def mpcStatus(self):
        status = subprocess.check_output(["mpc", "status"], stdin=None, stderr=None, shell=False, universal_newlines=False)
        print status
        
    def playCh1(self):
        status = subprocess.check_output(["mpc", "play", "1"], stdin=None, stderr=None, shell=False, universal_newlines=False)
        
    def playCh2(self):
        status = subprocess.check_output(["mpc", "play", "2"], stdin=None, stderr=None, shell=False, universal_newlines=False)

    def stopPlayer(self):
        status = subprocess.check_output(["mpc", "stop"], stdin=None, stderr=None, shell=False, universal_newlines=False)

def main():
    mpc = MpcCmd()
    GPIO.setmode(GPIO.BCM)  
    gpioId = [5, 6, 12, 13];
    gpioState = [];
    gpioNum = len(gpioId)
                       
    '''
    # GPIO reading code - ignore for now
    
    GPIO set up as inputs. All pulled up
    for i in range(gpioNum):
        GPIO.setup(gpioId[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
   
    for i in range(gpioNum):
        userCmd = userCmd + str(GPIO.input(gpioId[i]))
    print userCmd
    '''
    
    while True:
    
        userCmd = raw_input("Enter command: play(channel n), stop, status: ")

        if (userCmd == '0111') or (userCmd == 'play1'):
            mpc.playCh1()
        
        if (userCmd == '1011') or (userCmd == 'play2'):
            mpc.playCh2()

        if userCmd == 'stop':
            mpc.stopPlayer()

        if userCmd == 'status':
            mpc.mpcStatus()

if __name__ == '__main__':
    main()
