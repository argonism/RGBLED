import RPi.GPIO as GPIO
import time
import fullcolor_led
import random

def set_random_led(led):
    r = random.randint(0, 100)
    g = random.randint(0, 100)
    b = random.randint(0, 100)
    led.to(r, g, b)

pin = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

led = fullcolor_led.FullcolerLED(11, 12, 13)
pre_frame = False
cur_frame = False
try:
    while True:
        cur_frame = GPIO.input(pin) == GPIO.HIGH
        
        if cur_frame and not pre_frame:
            set_random_led(led)
        #     print("Pushed")
        # if not cur_frame and pre_frame:
        #     print("released")

        pre_frame = cur_frame
except KeyboardInterrupt:
    pass

GPIO.cleanup()