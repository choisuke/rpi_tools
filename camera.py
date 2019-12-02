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
        self.shot_and_save(self, name, cntr)

    def release(self):
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    front=camera(100, 100, 30, 1)
    for i in range(200):
        front.pass_frame(30)
        front.shot_and_save(str(i).zfill(10)[-2:]+'.png')
