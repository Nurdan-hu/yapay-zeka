import cv2
img2 = cv2.imread('resimler/sincap.webp', cv2.IMREAD_GRAYSCALE) #eğer resim bir klasörün içerisindeyse şu şekilde alabilirsin: resimler/sincap.webp
cv2.imshow('Deneme' , img2)
cv2.waitKey(0) #herhangi bir tuşa basılana kadar bekler.
cv2.destroyAllWindows()