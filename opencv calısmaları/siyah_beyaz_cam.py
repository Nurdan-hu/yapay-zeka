import cv2, numpy as np
video= cv2.VideoCapture(0)
while video.isOpened():
    ret, frame = video.read()
    newarr= np.hsplit(frame,2)
    newarr[0] = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    height, width = newarr[0].shape
    yenidenBoyutlandır = np.zeros((height, width, 3), dtype=np.uint8)
    yenidenBoyutlandır[:, :, 0] = newarr[1]  # Kırmızı kanal
    yenidenBoyutlandır[:, :, 1] = newarr[1]  # Yeşil kanal
    yenidenBoyutlandır[:, :, 2] = newarr[1]  # Mavi kanal
    if ret == True:
        gosterilecek= np.concatenate((newarr[0],newarr[1]) ,axis=1)
        tus = cv2.waitKey(1)
        if tus == ord('q'): 
                break
    else : 
        break
video.release
cv2.destroyAllWindows