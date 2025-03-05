import cv2

img1 = cv2.imread('resimler/sincap2.webp')
# roi = img1[y1:y2, x1:x2]
roi = img1[200:400, 200:400] # el,burun
# roi = img1[400:520, 400:650] # burun

cv2.imshow('parça',roi)
cv2.waitKey(0)
cv2.destroyAllWindows()