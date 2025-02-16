import cv2, random
import numpy as np
a = random.randint(0,255)
b = random.randint(0,255)
c = random.randint(0,255)
r1= np.full ((200,300,3) , [a,b,c] , dtype=np.uint8)
cv2.imshow("Resim",r1)
print(f"Mavi:{a}, Yeşil: {b} , Kırmızı: {c}")
cv2.waitKey(0)
cv2.destroyAllWindows()

