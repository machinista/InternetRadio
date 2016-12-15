#!/usr/bin/env python

def main():
    import RPi.GPIO as GPIO  
    GPIO.setmode(GPIO.BCM)  
    
    gpioId = [4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19,
    26, 14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21];
    
    # GPIO set up as inputs. All pulled up
    gpioNum = len(gpioId) - 1
    
    for i in range(gpioNum):
		GPIO.setup(gpioId[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    for i in range(gpioNum):
        if GPIO.input(gpioId[i]) == 1:
            print "GPIO %s: " % gpioId[i] + "high"
        else:
            print "GPIO %s: " % gpioId[i] + "low"

if __name__ == '__main__':
    main()
