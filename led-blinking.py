#led blinking

# import libraries
import RPi.GPIO as GPIO
import sleep from time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led = 21
sleepTime = 1

GPIO.setup(led, GPIO.OUT)

GPIO.output(led, False)

while True:
    GPIO.output(led, True)
    sleep(sleepTime)
    GPIO.output(led, False)
    sleep(sleepTime)