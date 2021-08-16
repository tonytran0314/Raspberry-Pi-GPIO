# press button to turn the led on

import RPi.GPIO as GPIO

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

        if (ledStatus == False) and (btnVal == False):
            GPIO.output(ledPin, True)
            ledStatus = True
        elif (ledStatus == True) and (btnVal == False):
            GPIO.output(ledPin, False)
            ledStatus = False

except KeyboardInterrupt:
    print("\nThe program has been stopped")

finally:
    GPIO.cleanup()
