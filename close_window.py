import cv2

def close ():
    while True :
        if cv2.waitKey(1) == 27 :
            break