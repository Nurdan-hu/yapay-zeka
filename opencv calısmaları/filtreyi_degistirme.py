import cv2, numpy as np
video= cv2.VideoCapture(0)
while video.isOpened():
    aa , alınanGörüntü = video.read()
    yeniDizi= np.hsplit(alınanGörüntü, 2)

    yükseklik , genişlik, renk = yeniDizi[1].shape

    yeniResim = np.full((yükseklik,genişlik,3), [99,99,99], dtype=np.uint8)
    yeniDizi[1]= np.add(yeniDizi[1], yeniResim)
    gosterilecek= np.concatenate((yeniDizi[0], yeniDizi[1]) ,axis=1)
    cv2.imshow("bilmemne" , gosterilecek)
    tus = cv2.waitKey(1)
    if tus == ord('q'): 
                break
video.release()
cv2.destroyAllWindows()
