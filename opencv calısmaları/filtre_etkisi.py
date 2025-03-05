import cv2

resim= cv2.imread('resimler/squirrel.webp')
x,y,r= resim.shape
print(resim.shape)
for a in range(x):
    for b in range(y):
        if resim[a][b][1] + 50 > 250 : resim [a][b][1] = 250
        else: resim [a][b][1] += 50

cv2.imshow('resim' , resim)
cv2.waitKey(0)