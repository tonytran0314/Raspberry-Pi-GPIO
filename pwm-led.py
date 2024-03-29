# adjust the brighteness of led

# Import the GPIO and time libraries
import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM and disable warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define pins
pwmPin = 18
GPIO.setup(pwmPin,GPIO.OUT)
pwm = GPIO.PWM(pwmPin,100)

# Make sure LED is off
pwm.start(0)

# Begin Loop
try:
    while True:
        # brighteness value
        count = 1
        
        # begin while loop to brighten LED
        while count < 100:
            # set duty cycle
            pwm.ChangeDutyCycle(count)

            # delay 1/100 of a second
            time.sleep(0.01)

            # increment count
            count = count + 1

        # begin while loop to dim LED
        while count > 1:
            pwm.ChangeDutyCycle(count)
            time.sleep(0.01)

            # set duty cycle
            pwm.ChangeDutyCycle(count)

            # delay 1/100 of a second
            time.sleep(0.01)

            # decrement count
            count = count - 1

except KeyboardInterrupt:  
    # here you put any code you want to run before the program   
    # exits when you press CTRL+C  
    print("\nThe program has been stopped")

finally:  
    GPIO.cleanup() # this ensures a clean exit   
