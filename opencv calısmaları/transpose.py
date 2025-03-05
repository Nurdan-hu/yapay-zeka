import cv2, numpy as np

vid = cv2.VideoCapture(0)
while vid.isOpened():
    ret, yakalananreim= vid.read()
    cv2.imshow("Orjinal Goruntu", yakalananreim)

    cv2.imshow("Traspose", cv2.transpose(yakalananreim))

    if cv2.waitKey(1) == ord('q'): 
                break
vid.release()
cv2.destroyAllWindows()