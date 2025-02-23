import numpy as np, cv2
cap= cv2.VideoCapture('wildlife2.mp4')
while cap.isOpened():
    ret, yakalananresim = cap.read()
    newarr= np.array_split(yakalananresim,2) #eğer np.hsplit(img,2) yazarsak dikey olarak böler
    cv2.imshow('Deneme1',newarr[0])
    cv2.imshow('Deneme2',newarr[1])
    if ret == True:
            # cv2.imshow('CANIMVIDEOM', yakalananresim)
            tus = cv2.waitKey(1)
            if tus == ord('q'): 
                break
    else : 
        break
cap.release
cv2.destroyAllWindows