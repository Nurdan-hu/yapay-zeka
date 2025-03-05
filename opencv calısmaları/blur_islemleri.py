# [250,250,250]
# [50,50,50]
# [200,200,100]

import cv2, numpy as np
vid= cv2.VideoCapture(0)
while vid.isOpened():
    ret , goruntu= vid.read()
    cv2.imshow('orjinal' , goruntu)
    blurluversiyon= cv2.GaussianBlur(goruntu,(7,7),0)
    cv2.imshow('ynei' , blurluversiyon)

    if cv2.waitKey(1)== ord("q"): break

vid.release()
cv2.destroyAllWindows()
