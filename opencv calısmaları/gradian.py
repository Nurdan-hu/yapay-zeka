import cv2, numpy as np

img1 = cv2.imread("resimler/squirrel.webp")
img1 = cv2.resize(img1, (512,512))

hsv = cv2.cvtColor(img1 , cv2.COLOR_BGR2HSV)

blue1= np.array([100,0,0])
blue2= np.array([255,255,255])

mask = cv2.inRange(hsv,blue1,blue2)

res = cv2.bitwise_and(img1,img1,mask=mask)
kernel = np.ones((5,5), np.uint8)

graident = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('original' , img1)
cv2.imshow('final image' , graident)

cv2.waitKey(0)
cv2.destroyAllWindows()