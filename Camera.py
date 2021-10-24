import imagezmq
import cv2
import time

sender = imagezmq.ImageSender(connect_to='tcp://192.168.50.152:5555')
rpi_name = "cam1" # send RPi hostname with each image
# setup camera params


cap = cv2.VideoCapture(0)

cap.open(0, apiPreference=cv2.CAP_V4L2)

cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
cap.set(cv2.CAP_PROP_FPS, 24.0)

while cap.isOpened():
    success, image = cap.read()
    #cv2.imwrite("/mnt/minty/image.jpg", image)
    response = sender.send_image(rpi_name, image)
    if response != b'OK':
        break


cap.release()