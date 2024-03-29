#!/usr/bin/env python
# coding: utf-8

import cv2

class camera:
    def __init__(self, width, height, fps=30, camnum=0):
        self.cap = cv2.VideoCapture(camnum)
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
        if ret:
            return self.frame
        else:
            self.shot()

    def pass_frame(self, num_frame):
        for i in range(num_frame):
            _, self.frame = self.cap.read()
        return

    def shot_and_save(self, name, gray=False, cntr=0):
        if cntr>=5:
            print('check camera again...')
            return False
        ret, self.frame = self.cap.read()
        if gray:
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_RGB2GRAY)
        if ret:
            cv2.imwrite(name, self.frame)
            return self.frame
        else:
            cntr+=1
        self.shot_and_save(self, name, cntr)

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    webcam=camera(100, 100, 30, 1)
    for i in range(200):
        webcam.pass_frame(30)
        webcam.shot_and_save(str(i).zfill(10)[-2:]+'.png')
