import numpy as np, cv2
img= cv2.imread('mavilogo.png')
height , width, channels = img.shape
for x in range(height):
    for y in range(width):
        if img[x,y][0]>50 and img[x,y][0]<200:
            img[x,y] = [0,0,255]
cv2.imshow('resim' , img)
cv2.waitKey(0)
cv2.destroyAllWindows