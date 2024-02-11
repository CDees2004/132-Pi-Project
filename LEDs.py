
# Name: Mars
# Date: 2 - 8 - 24
# Desc:
#software that constantly fades through all colors 
# in a constant loop, this will either be playing on a separate pi
# constantly or heavily altered and made to flash when image is captured
# which is done will depend on the implementation details 

import colorsys
import RPi.GPIO as GPIO
from time import sleep

# disabling the several warnings that appear everytime it is ran 
GPIO.setwarnings(False)

# RGB LED 1
RED_PIN1 = 18
GREEN_PIN1 = 19
BLUE_PIN1 = 20

# RGB LED 2
RED_PIN2 = 21
GREEN_PIN2 = 22
BLUE_PIN2 = 23

# RGB LED 3
RED_PIN3 = 24
GREEN_PIN3 = 25
BLUE_PIN3 = 26

# RGB LED 4
RED_PIN4 = 13
GREEN_PIN4 = 12
BLUE_PIN4 = 6

BUTTON_PIN = 5

GPIO.setmode(GPIO.BCM)

# setting up GPIO pins for RGB LEDs
GPIO.setup(RED_PIN1, GPIO.OUT)
GPIO.setup(GREEN_PIN1, GPIO.OUT)
GPIO.setup(BLUE_PIN1, GPIO.OUT)

GPIO.setup(RED_PIN2, GPIO.OUT)
GPIO.setup(GREEN_PIN2, GPIO.OUT)
GPIO.setup(BLUE_PIN2, GPIO.OUT)

GPIO.setup(RED_PIN3, GPIO.OUT)
GPIO.setup(GREEN_PIN3, GPIO.OUT)
GPIO.setup(BLUE_PIN3, GPIO.OUT)

GPIO.setup(RED_PIN4, GPIO.OUT)
GPIO.setup(GREEN_PIN4, GPIO.OUT)
GPIO.setup(BLUE_PIN4, GPIO.OUT)

GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# setting up pmw channels for RGB LEDs
RED_PWM1 = GPIO.PWM(RED_PIN1, 100)
GREEN_PWM1 = GPIO.PWM(GREEN_PIN1, 100)
BLUE_PWM1 = GPIO.PWM(BLUE_PIN1, 100)

RED_PWM2 = GPIO.PWM(RED_PIN2, 100)
GREEN_PWM2 = GPIO.PWM(GREEN_PIN2, 100)
BLUE_PWM2 = GPIO.PWM(BLUE_PIN2, 100)

RED_PWM3 = GPIO.PWM(RED_PIN3, 100)
GREEN_PWM3 = GPIO.PWM(GREEN_PIN3, 100)
BLUE_PWM3 = GPIO.PWM(BLUE_PIN3, 100)

RED_PWM4 = GPIO.PWM(RED_PIN4, 100)
GREEN_PWM4 = GPIO.PWM(GREEN_PIN4, 100)
BLUE_PWM4 = GPIO.PWM(BLUE_PIN4, 100)

# intitially start with pwn with 0% duty cycle
RED_PWM1.start(0)
GREEN_PWM1.start(0)
BLUE_PWM1.start(0)

RED_PWM2.start(0)
GREEN_PWM2.start(0)
BLUE_PWM2.start(0)

RED_PWM3.start(0)
GREEN_PWM3.start(0)
BLUE_PWM3.start(0)

RED_PWM4.start(0)
GREEN_PWM4.start(0)
BLUE_PWM4.start(0)

# function that sets the color of the lights 

def set_rainbow_color(pwm_red, pwm_green, pwm_blue, hue):
    rgb = colorsys.hsv_to_rgb(hue / 360.0, 1.0, 1.0)
    pwm_red.ChangeDutyCycle(rgb[0] * 100)
    pwm_green.ChangeDutyCycle(rgb[1] * 100)
    pwm_blue.ChangeDutyCycle(rgb[2] * 100)

# function responsible for actually enabling the lights 
def set_leds_off():
    # set all of the pw, duty cycles to 0 to turn off the LEDs
    RED_PWM1.ChangeDutyCycle(0)
    GREEN_PWM1.ChangeDutyCycle(0)
    BLUE_PWM1.ChangeDutyCycle(0)

    RED_PWM2.ChangeDutyCycle(0)
    GREEN_PWM2.ChangeDutyCycle(0)
    BLUE_PWM2.ChangeDutyCycle(0)

    RED_PWM3.ChangeDutyCycle(0)
    GREEN_PWM3.ChangeDutyCycle(0)
    BLUE_PWM3.ChangeDutyCycle(0)

    RED_PWM4.ChangeDutyCycle(0)
    GREEN_PWM4.ChangeDutyCycle(0)
    BLUE_PWM4.ChangeDutyCycle(0)

try:        # I have to lookup what this does everytime LEDs are used 
    hue = 0
    while True:
        set_rainbow_color(RED_PWM1, GREEN_PWM1, BLUE_PWM1, hue)
        set_rainbow_color(RED_PWM2, GREEN_PWM2, BLUE_PWM2, hue)
        set_rainbow_color(RED_PWM3, GREEN_PWM3, BLUE_PWM3, hue)
        set_rainbow_color(RED_PWM4, GREEN_PWM4, BLUE_PWM4, hue)
        
        hue += 1
        if hue > 360:
            hue = 0

        # Check if the button is pressed
        # THIS IS THE ONE !!!!!!!!!!!!!!!!!!!!!!!
        if GPIO.input(BUTTON_PIN) == GPIO.HIGH:     # based on idea user would disable the buttons with GPIO input, probably wont be used
            set_leds_off()
            sleep(1)  # delay to avoid rapid on/off due to button press sensitivity

        sleep(0.02)

except KeyboardInterrupt:
    pass

finally:
    # stop the pwm and clean up GPIO
    RED_PWM1.stop()
    GREEN_PWM1.stop()
    BLUE_PWM1.stop()

    RED_PWM2.stop()
    GREEN_PWM2.stop()
    BLUE_PWM2.stop()

    RED_PWM3.stop()
    GREEN_PWM3.stop()
    BLUE_PWM3.stop()

    RED_PWM4.stop()
    GREEN_PWM4.stop()
    BLUE_PWM4.stop()

    GPIO.cleanup()
