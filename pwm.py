import RPi.GPIO as GPIO
import time

red_pin = 11
blue_pin =  12
green_pin = 13


GPIO.setmode(GPIO.BOARD)
GPIO.setup(red_pin,GPIO.OUT)
GPIO.setup(blue_pin,GPIO.OUT)
GPIO.setup(green_pin,GPIO.OUT)

GPIO.output(red_pin, GPIO.LOW)  
GPIO.output(blue_pin, GPIO.LOW)  
GPIO.output(green_pin, GPIO.LOW)  


red = GPIO.PWM(red_pin, 1000)
blue = GPIO.PWM(blue_pin, 1000)
green = GPIO.PWM(green_pin, 1000)

red.start(0)
blue.start(0)
green.start(0)

leds = [red, green, blue]

try:
    while True:
        for i in range(len(leds)):
            for dc in range(0, 101, 4):
                leds[i].ChangeDutyCycle(dc)
                time.sleep(0.05)

            for dc in range(0, 101, 4):
                if i == 0:
                    leds[len(leds)-1].ChangeDutyCycle(100 - dc)
                else:
                    leds[i-1].ChangeDutyCycle(100 - dc)
                time.sleep(0.05)


except KeyboardInterrupt:
    for led in leds:
        led.stop()
        
    GPIO.output(red_pin, GPIO.HIGH)  
    GPIO.output(blue_pin, GPIO.HIGH)  
    GPIO.output(green_pin, GPIO.HIGH)  

    GPIO.cleanup()