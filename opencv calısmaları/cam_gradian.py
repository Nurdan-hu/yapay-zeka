import cv2, numpy as np

vid = cv2.VideoCapture(0)

while vid.isOpened():
    ret , img= vid.read()
    t_lower = 100
    t_upper=200 
    aperture_size = 3
    img= cv2.resize(img,(750,500))
    edge= cv2.Canny(img, t_lower, t_upper,
                    apertureSize=aperture_size)
    cv2.imshow('edge',edge)
    if cv2.waitKey(1)== ord("q"): break
vid.release()
cv2.destroyAllWindows()
