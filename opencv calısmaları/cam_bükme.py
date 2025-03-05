import cv2, numpy as np
vid= cv2.VideoCapture(0)
while vid.isOpened():
    ret, goruntu= vid.read()
    cv2.imshow("orjınal goruntu" , goruntu)
    sutun, satir = goruntu.shape[:2]

    donmesekli= cv2.getRotationMatrix2D((satir//4,sutun//4),30,1)
    donmussekil= cv2.warpAffine(goruntu,donmesekli,(satir,sutun))

    cv2.imshow(" goruntu" , donmussekil)

    if cv2.waitKey(1)== ord("q"): break
vid.release()
cv2.destroyAllWindows()
