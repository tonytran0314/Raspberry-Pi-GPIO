#led blinking

# import libraries
import RPi.GPIO as GPIO
from time import sleep

#set mode and switch off warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# define pins and sleep time (second)
led = 21
sleepTime = 1

# set led pin as output pin
GPIO.setup(led, GPIO.OUT)

# Turn led off first
GPIO.output(led, False)

try: 
    while True:
        #led on for 1 sec
        GPIO.output(led, True)
        sleep(sleepTime)
        #led off for 1 sec
        GPIO.output(led, False)
        sleep(sleepTime)
       
#except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  
#    print("Hello")

finally:  
    GPIO.cleanup() # this ensures a clean exit  
