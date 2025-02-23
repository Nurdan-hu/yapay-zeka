import cv2
img = cv2.imread('resimler/sincap.webp', 0)
tus = cv2.waitKey(0)
cv2.imwrite('resimler/sincap2.webp',img)
cv2.destroyAllWindows() 