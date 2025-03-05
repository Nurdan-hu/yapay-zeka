import cv2
import numpy as np

r1 = cv2.imread("resimler/squirrel.webp")
r2 = cv2.imread("resimler/galata.jpg")
cv2.imshow("Orjinal1", r1)
cv2.imshow("Orjinal2", r2)

# np.array([hue, saturation, value])
alt = np.array([80,40,50]) # lower
ust = np.array([100,50,255]) # upper

_, c1 = cv2.threshold(r2, 200, 255, cv2.THRESH_BINARY)
_, c2 = cv2.threshold(r2, 200, 255, cv2.THRESH_BINARY_INV)

c3 = cv2.cvtColor(c1, cv2.COLOR_BGR2HSV)
cv2.imshow("Cevrilmis1", c1)
cv2.imshow("Cevrilmis2", c2)
cv2.imshow("Cevrilmis3", c3)
cv2.imwrite('resimler/güzelglt.webp',c1)

f1 = cv2.inRange(c3, alt, ust)
cv2.imshow("inRange ile", f1)

cv2.waitKey(0)
cv2.destroyAllWindows()
