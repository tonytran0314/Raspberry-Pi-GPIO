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

# Turn led off first
GPIO.output(led, False)

# Loop that turn led on and off
while True:
    #led on for 1 sec
    GPIO.output(led, True)
    sleep(sleepTime)
    #led off for 1 sec
    GPIO.output(led, False)
    sleep(sleepTime)
    GPIO.output(led, True)
    sleep(sleepTime)

