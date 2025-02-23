import numpy as np, cv2
cap= cv2.VideoCapture(0)
while cap.isOpened():
    ret, yakalananresim = cap.read()
    newarr= np.hsplit(yakalananresim,2)
    if ret == True:
        cv2.imshow('Deneme1',newarr[0])
        cv2.imshow('Deneme2',newarr[1])            
        tus = cv2.waitKey(1)
        if tus == ord('q'): 
                break
    else : 
        break
cap.release
cv2.destroyAllWindows