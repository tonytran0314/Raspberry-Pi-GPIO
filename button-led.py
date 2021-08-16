# press button to turn the led on

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

btnPin = 17
ledPin = 21
GPIO.setup(btnPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(ledPin, GPIO.OUT)

GPIO.output(ledPin, False)
ledStatus = False

try:
    while True:
        btnVal = GPIO.input(btnPin)

        if (btnVal == False):
            print("Button pressed")
            if (ledStatus == False):
                ledStatus = True
                GPIO.output(ledPin, True)
            else:
                ledStatus = False
                GPIO.output(ledPin, False)
except KeyboardInterrupt:
    print("The program has been stopped")
finally:
    GPIO.cleanup()
