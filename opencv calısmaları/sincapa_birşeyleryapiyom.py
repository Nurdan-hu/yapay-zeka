import cv2
img1 = cv2.imread('resimler/sincap2.webp')
img2 = cv2.imread('resimler/sincap2.webp',0)

# item
x = 100
y = 100
print(f'{x}, {y} noktası Blue  : ', img1.item(x,y,0))
print(f'{x}, {y} noktası Green : ', img1.item(x,y,1))
print(f'{x}, {y} noktası Red   : ', img1.item(x,y,2))
