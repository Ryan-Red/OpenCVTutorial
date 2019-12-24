import cv2
import numpy as np

input_image = cv2.imread("C:/Users/Ryan/source/repos/OpenCVTutorial/images/input.jpg")

cv2.imshow('Hello World', input_image)
cv2.waitKey(0)
cv2.destroyAllWindows()