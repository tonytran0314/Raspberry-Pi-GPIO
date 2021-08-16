# press button to turn the led on

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

btnPin = 17
GPIO.setup(btnPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
    #while True:
    btnVal = GPIO.input(btnPin)

    if (btnVal == False):
        print("Button pressed")
except KeyboardInterrupt:
    print("The program has been stopped")
finally:
    GPIO.cleanup()
