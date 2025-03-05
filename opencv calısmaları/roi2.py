import cv2, random, numpy as np

video= cv2.VideoCapture(0)
while video.isOpened():
    ret, yakalananresim = video.read()
    x,y,r= yakalananresim.shape

    parca= yakalananresim[100:300, 400:600]
    parcas= np.full((100,100,3),[0,0,0] , dtype=np.uint8)
    parcas[20:]
    yakalananresim[50:150, 50:150] = parcas
    cv2.imshow('resim' , yakalananresim)


    if cv2.waitKey(1)== ord('q'): 
                break
video.release()
cv2.destroyAllWindows()