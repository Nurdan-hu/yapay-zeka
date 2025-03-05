import cv2

img1 = cv2.imread('resimler/sincap2.webp')

# img1[y1:y2, x1:x2,BGR indisi] = yenideger
# img1[:,:,0] =  # Blue değerlerini 0 yap
img1[:,:,1] = 0 # Green değerlerini 0 yap
img1[:,:,2] = 0 # Red değerlerini 0 yap

cv2.imshow('filtreli',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
