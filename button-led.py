# press button to turn the led on

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(BCM)
GPIO.setwarnings(False)

btnPin = 20
GPIO.setup(btnPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
    btnVal = GPIO.input(btnPin)

    if (btnVal == False):
        print("Button pressed")
