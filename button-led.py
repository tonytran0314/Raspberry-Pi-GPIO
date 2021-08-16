# press button to turn the led on and off

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

btnPin = 5
ledPin = 22
GPIO.setup(btnPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(ledPin, GPIO.OUT)

GPIO.output(ledPin, False)
ledStatus = False
btnVal = True

try:
    while True:
        btnVal = GPIO.input(btnPin)

        if (btnVal == False) and (ledStatus == False):
            GPIO.output(ledPin, True)
            print("LED ON")
            ledStatus = True
            sleep(0.5)
        elif (btnVal == False) and (ledStatus == True):
            GPIO.output(ledPin, False)
            print("LED OFF")
            ledStatus = False
            sleep(0.5)
        sleep(0.1)

except KeyboardInterrupt:
    print("\nThe program has been stopped")

finally:
    GPIO.cleanup()
