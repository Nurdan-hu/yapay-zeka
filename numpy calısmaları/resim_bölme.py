import numpy as np, cv2
img= cv2.imread('resimler/bayrak1.jpg')
# cv2.imshow('Deneme',img)
newarr= np.array_split(img,2) #eğer np.hsplit(img,2) yazarsak dikey olarak böler
cv2.imshow('Deneme1',newarr[0])
cv2.imshow('Deneme2',newarr[1])
cv2.waitKey(0) # 3 saniye bekle
cv2.destroyAllWindows() # pencereleri kap