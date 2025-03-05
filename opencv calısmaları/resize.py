import cv2,random, numpy as np

video = cv2.VideoCapture(0) 
while video.isOpened():
    ret, yakalananresim= video.read()
    x,y,r= yakalananresim.shape

    cv2.imshow('resim',yakalananresim)
    yenisekil = cv2.resize(yakalananresim,(x//2,y//2))
    cv2.imshow('resim2',yenisekil)
    if cv2.waitKey(1)== ord('q'): 
                break
video.release()
cv2.destroyAllWindows()