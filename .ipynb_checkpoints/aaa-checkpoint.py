# coding: utf-8
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
 
        self.cap.release()
        cv2.destroyAllWindows()
        return
    
    def shot(self):
        self.ret, self.frame = self.cap.read()
        return self.ret

    def save(self, name):
        if self.ret:
            cv2.imwrite(name, self.frame)
        return self.ret

    def shot_and_save(self, name, cntr=0):
        if cntr>=5:
            print('check camera again...')
            return
        
        self.ret, self.frame = self.cap.read()
        if self.ret:
            cv2.imwrite(name, self.frame)
            return
        else:
            cntr+=1

        shot_and_save(self, name, cntr)
    
    def release(self):
        self.cap.release()

if __name__ == '__main__':
    front=camera(100, 100, 100)
    for i in range(10):
        front.shot_and_save(str(i).zfill(3) + '.png')
