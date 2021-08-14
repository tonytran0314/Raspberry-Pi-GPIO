#led blinking

# import libraries
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# define pins and sleep time (second)
led = 21
sleepTime = 1

# set led pin as output pin
GPIO.setup(led, GPIO.OUT)

GPIO.output(led, False)

while True:
    GPIO.output(led, True)
    sleep(sleepTime)
    GPIO.output(led, False)
    sleep(sleepTime)
