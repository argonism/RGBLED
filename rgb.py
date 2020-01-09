import RPi.GPIO as GPIO
import time
from enum import Enum
import sys

red_pin = 11
blue_pin =  12
green_pin = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(red_pin,GPIO.OUT)
GPIO.setup(blue_pin,GPIO.OUT)
GPIO.setup(green_pin,GPIO.OUT)


class Color(Enum):
    Red = 1
    Blue = 2
    Green = 3

    @classmethod
    def value_of(cls, target_value):
        for e in Color:
            if e.name == target_value:
                return e
        raise ValueError('{} は有効な乗り物の値ではありません'.format(target_value))


def led_switch(color):
    if color == Color.Red:
        GPIO.output(red_pin,False)
        GPIO.output(blue_pin,True)
        GPIO.output(green_pin,True)
        print("Turn on Red")

    elif color == Color.Blue:
        GPIO.output(red_pin, True)
        GPIO.output(blue_pin,False)
        GPIO.output(green_pin, True)
        print("Turn on Blue")        

    elif color == Color.Green:
        GPIO.output(red_pin, True)
        GPIO.output(blue_pin,True)
        GPIO.output(green_pin,False)
        print("Turn on Green")


# led_switch(Color.value_of(sys.argv[1]))
GPIO.output(red_pin, True)
GPIO.output(blue_pin,True)
GPIO.output(green_pin,True)

p = GPIO.PWM(green_pin, 0)

p.start(0)
time.sleep(5)
p.stop()
# GPIO.output(red_pin, True)
# GPIO.output(blue_pin,True)
# GPIO.output(green_pin,True)