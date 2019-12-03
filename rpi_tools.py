#!/usr/bin/env python
# coding: utf-8

# RaspberryPi Tools

import ftplib
from camera import camera
def ftp_upload(hostname, username, passwd, upload_file, upload_path):
    file = open(upload_file, 'rb')
    ftp = ftplib.FTP(hostname, username, passwd=passwd)
    code = ftp.storbinary(upload_path, file)
    ftp.close()
    file.close()

    return code

if __name__ == '__main__':
    webcam=camera(100, 100, 30, 0)
    for i in range(200):
        webcam.shot_and_save(str(i).zfill(10)[-2:]+'.png')
        webcam.pass_frame(30)
