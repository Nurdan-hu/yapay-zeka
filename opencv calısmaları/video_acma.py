import cv2
cap = cv2.VideoCapture('wildlife2.mp4')
while cap.isOpened():
    ret, yakalananresim = cap.read()
    yakalananresim[10,10]=[0,0,255]
    yakalananresim[10,11]=[0,0,255]
    yakalananresim[10,12]=[0,0,255]
    yakalananresim[11,10]=[0,0,255]
    yakalananresim[11,11]=[0,0,255]
    yakalananresim[11,12]=[0,0,255]

    if ret == True:
        cv2.imshow('CANIMVIDEOM', yakalananresim)
        tus = cv2.waitKey(1)
        if tus == ord('q'): break
    else : 
        break
cap.release
cv2.destroyAllWindows