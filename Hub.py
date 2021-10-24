# run this program on the Mac to display image streams from multiple RPis
import cv2
import imagezmq
image_hub = imagezmq.ImageHub()
index=0
while True:  # show streamed images until Ctrl-C
    rpi_name, image = image_hub.recv_image()
    cv2.imwrite(f"/tmp/output/{index}.jpg", image)
    image_hub.send_reply(b'OK')
    index = index + 1