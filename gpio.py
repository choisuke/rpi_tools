#!/usr/bin/env python
# coding: utf-8

## GPIOに関するクラス
import RPi.GPIO as GPIO

class GPIO_led:
    def __init__(self, pin_num):
        self.pin_num = pin_num
        self.GPIO = GPIO
        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setup(self.pin_num, self.GPIO.OUT)
        
    def led_ctl(self, flg):
        if flg:
            self.GPIO.output(self.pin_num, self.GPIO.HIGH)
        else:
            self.GPIO.output(self.pin_num, self.GPIO.LOW)

if __name__ == '__main__':
    front_led=GPIO_led(1)
    for i in range(100):
        front_led.led_ctl(True)
        front_led.led_ctl(False)