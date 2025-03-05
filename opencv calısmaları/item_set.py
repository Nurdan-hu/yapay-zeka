import cv2, numpy as np

img1 = cv2.imread('resimler/sincap2.webp')

for a in range(50,80):
    for b in range(50,80):
        img1[a,b,0]= 255 # 1 Blue max=255
        img1[a,b,1]= 0 # 2 Green max=255
        img1[a,b,2] = 0 # 3 Red max=255

cv2.imshow('değişiklik',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()