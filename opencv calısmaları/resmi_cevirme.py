import numpy as np, cv2
img=cv2.imread('resimler/yesil.jpeg')
height , width, channels= img.shape
for x in range (height):
    for y in range(width):
        if img[x,y][0]> 50 and img [x,y][0]< 200:
            img[x,y] = [0,0,255]
cv2.imshow('Deneme' , img)
cv2.waitKey(1000)
cv2.destroyAllWindows()