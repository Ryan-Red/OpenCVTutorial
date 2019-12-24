
import cv2

img = cv2.imread(path + "/images/input.jpg",0) #0 is to greyscale the image automatically

cv2.imshow('Greyscaled',img)
cv2.waitKey(0)
cv2.destroyAllWindows()