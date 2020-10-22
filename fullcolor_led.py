import RPi.GPIO as GPIO
import time
import random

class FullcolerLED():
    def __init__(self, red_pin, green_pin, blue_pin):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(red_pin,GPIO.OUT)
        GPIO.setup(blue_pin,GPIO.OUT)
        GPIO.setup(green_pin,GPIO.OUT)

        GPIO.output(red_pin, GPIO.LOW)  
        GPIO.output(blue_pin, GPIO.LOW)  
        GPIO.output(green_pin, GPIO.LOW)  

        self.red = GPIO.PWM(red_pin, 1000)
        self.blue = GPIO.PWM(blue_pin, 1000)
        self.green = GPIO.PWM(green_pin, 1000)

        self.red.start(0)
        self.blue.start(0)
        self.green.start(0)

        self.r = 0
        self.g = 0
        self.b = 0
    
    def set_duty_cycle(self, led, dc):
        led.ChangeDutyCycle(dc)
        time.sleep(0.01)

    def to(self, red, green, blue):
        linear = self.linear(red, green, blue)
        try:
            for r, g, b in linear:
                self.set_duty_cycle(self.red, r)
                self.set_duty_cycle(self.green, g)
                self.set_duty_cycle(self.blue, b)
        except KeyboardInterrupt:
            self.red.stop()
            self.blue.stop()
            self.green.stop()
              
            GPIO.cleanup()


    def linear(self, r, g, b):
        def calc_color(current, target, degree):
            if abs(target - current) < degree:
                return target
            else:
                return current + degree if target > current else current - degree

        degree = 2
        change = True
        # new_r,new_g, new_b = self.r, self.g, self.b
        while change:
            self.r = calc_color(self.r, r, degree)
            self.g = calc_color(self.g, g, degree)
            self.b = calc_color(self.b, b, degree)

            print(self.r, self.g, self.b)

            yield self.r,self.g, self.b

            if self.r == r and self.g == g and self.b == b:
                change = False

if __name__ == "__main__":
    led = FullcolerLED(11, 12, 13)
    # while True:
    r = random.randint(0, 100)
    g = random.randint(0, 100)
    b = random.randint(0, 100)
    led.to(r, g, b)