#!/usr/bin/python3
"""
Names: Inessa Rajah
Student Number: RJHINE001
Prac: 1
Date: <22/01/2019>
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time
x =0
#set counter to 0 initially
from itertools import product
LED_pins = [23, 24, 25] #array of LED pins
btn_pins = [5, 6] #array of button pins
values = list(product([1,0], repeat=3)) #create array of possible binary values
GPIO.setmode(GPIO.BCM) #set pin mode
GPIO.setup(LED_pins, GPIO.OUT) #set pins connected to LEDs (pins 23, 24, 25) as output pins
GPIO.output(LED_pins, 0) #make outputs to LED pins 0 initially
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP) #set pins connected to buttons (pins 5,6) input pins with pull up resistors
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)



def main():
	pass
	
def button1(pin):
        global x
        x= x+1  #if press button1 (connected to pin 5), increment counter by 1
        display() #call display function

def button2(pin):
        global x
        x= x-1 #if press button2 (connected to pin 6), increment counter by 1
        display() #call display function

def display():
        global x
        if x==8: #if counter is 8 (cannot be displayed by 3 bits), set it back to 0
                x=0
        if x<0: #if counter is negative, set counter to 7 (highest possible value that can be displayed by 3 bits)
                x = len(values)-1

        i=len(values) - (x+1)
        GPIO.output(LED_pins, values[i]) #show binary number on LEDs




GPIO.add_event_detect(5, GPIO.FALLING, callback=button1, bouncetime=150) #when button connected to pin 5 is pressed, increment LED value by 1 by calling button1 
GPIO.add_event_detect(6, GPIO.FALLING, callback=button2, bouncetime=150)	#when button connected to pin 6 is pressed, decrement LED value by 1 by calling button2


# Only run the functions if main 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
            #GPIO.cleanup()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)

