import cv2

video= cv2.VideoCapture(0)
while video.isOpened():
    ret, yakalananResim= video.read()
    cv2.imshow('tümresim' , yakalananResim)
    parca = yakalananResim[50:250,50:250]
    cv2.imshow('parcası' , parca)
    if cv2.waitKey(1)== ord('q'): 
                break
video.release()
cv2.destroyAllWindows()