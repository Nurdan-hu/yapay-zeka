import numpy as np, cv2
vid= cv2.VideoCapture(0)
while vid.isOpened():
    ret, yakalananresim = vid.read()    
    resim = np.zeros((400,600,3),np.uint8)     
    yenivid=cv2.circle(yakalananresim,(300,200),100,(255,255,255),2)
    cv2.imshow('sy' , yenivid)
    if  cv2.waitKey(1) == ord('q'): break
vid.release()
cv2.destroyAllWindows()