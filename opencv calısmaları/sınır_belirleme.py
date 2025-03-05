import cv2

img = cv2.imread("resimler/galata2.png") # Read image

# Setting All parameters
t_lower = 100 # Lower Threshold
t_upper = 200 # Upper threshold
aperture_size = 3 # Aperture size
img=cv2.resize(img, (180,270))

# Applying the Canny Edge filter
# with Custom Aperture Size
edge = cv2.Canny(img, t_lower, t_upper,
                apertureSize=aperture_size)
cv2.imshow('original', img)
cv2.imshow('edge', edge)
cv2.waitKey(0)
cv2.destroyAllWindows()