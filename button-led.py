# press the button to turn the led on and off

# import libraries
import RPi.GPIO as GPIO
from time import sleep

# set BCM mode and turn off warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# pins declaration
btnPin = 5
ledPin = 22
# pins function declaration
GPIO.setup(btnPin, GPIO.IN, pull_up_down = GPIO.PUD_UP) # GPIO 22 as a input pin (a button) 
GPIO.setup(ledPin, GPIO.OUT) # GPIO 5 as a output pin (a led)

# turn led off first
GPIO.output(ledPin, False)

#set the led status is False = when the led is off 
ledStatus = False

#set button status is True = UP (the button hasn't been pressed)
btnVal = True

try:
    while True:
        #set button value = value that collect from pin 22 
        btnVal = GPIO.input(btnPin)

        # if I press the button and the led is off
        # then turn the led on and set led status to True
        if (btnVal == False) and (ledStatus == False):
            GPIO.output(ledPin, True)
            print("LED ON")
            ledStatus = True
            sleep(0.5)
        
        # if I press the button and the led is on
        # then turn the led off and set led status to False
        elif (btnVal == False) and (ledStatus == True):
            GPIO.output(ledPin, False)
            print("LED OFF")
            ledStatus = False
            sleep(0.5)
        sleep(0.1)

# print this when I press Ctrl+C
except KeyboardInterrupt:
    print("\nThe program has been stopped")

# clean all things when end the program
finally:
    GPIO.cleanup()
