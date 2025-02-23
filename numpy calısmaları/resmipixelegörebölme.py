import numpy as np, cv2
img= cv2.imread('resimler/bayrak1.jpg')
# cv2.imshow('Deneme',img)
yeniresm = img[:100:] 
cv2.imshow('Deneme',yeniresm)
cv2.waitKey(0) # 3 saniye bekle
cv2.destroyAllWindows() # pencereleri kap