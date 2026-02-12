from machine import Pin, PWM
from time import sleep


class Servo():
    def __init__(self, pin):
        self.pwm = PWM(Pin(pin))
        self.pwm.freq(50)
        
        self.min_duty = 1639
        self.max_duty = 8192
        
        self.angle = 90
        
    def set_angle(self, angle):
        angle = max(0, min(180, angle))
        self.angle = angle
        duty = int(self.min_duty + (angle / 180) * (self.max_duty - self.min_duty))
        self.pwm.duty_u16(duty)