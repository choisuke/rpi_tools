#!/usr/bin/env python
# coding: utf-8

# RaspberryPi Tools


## GPIOに関するクラス
import RPi.GPIO as GPIO

class GPIO_led:
    def __init__(self, pin_num):
        self.pin_num = pin_num
        self.GPIO = GPIO
        self.GPIO.setmode(self.GPIO.BCM)
        self.GPIO.setup(self.pin_num, self.GPIO.OUT)
        
    def led_on(self):
        self.GPIO.output(self.pin_num, self.GPIO.HIGH)

    def led_off(self):
        self.GPIO.output(self.pin_num, self.GPIO.HIGH)


## OpenCV のカメラに関するクラス
import cv2

class camera:
    def __init__(self, width, height, fps=4):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3,width)
        self.cap.set(4,height)
        self.cap.set(5,fps) # FPS
    
    def realtime(self):
        while(self.cap.isOpened()):
            _, self.frame = self.cap.read()
            cv2.imshow('frame',self.frame)
            if cv2.waitKey(1) != -1:
                break
        return
    
    def shot(self):
        ret, self.frame = self.cap.read()
        return ret

    def pass_frame(self, num_frame):
        for i in range(num_frame):
            _, self.frame = self.cap.read()
        return

    def shot_and_save(self, name, cntr=0):
        if cntr>=5:
            print('check camera again...')
            return False
        
        ret, self.frame = self.cap.read()
        if ret:
            cv2.imwrite(name, self.frame)
            return True
        else:
            cntr+=1

        shot_and_save(self, name, cntr)
    
    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()

import ftplib
def ftp_upload(hostname, username, passwd, upload_file, upload_path):
    ftp = ftplib.FTP(hostname, username, passwd=passwd)
    file = open(upload_file, 'rb')
    code = ftp.storbinary(upload_path, file)
    
    file.close()
    ftp.close()
    
    return code

if __name__ == '__main__':
    front=camera(100, 100, 100)
    for i in range(200):
        front.shot_and_save(str(i).zfill(10)[-2:]+'.png')
        front.pass_frame(30)

