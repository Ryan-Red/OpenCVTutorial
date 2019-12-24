import cv2
import numpy as np
global path

path = "C:/Users/Ryan/source/repos/OpenCVTutorial"
input_image = cv2.imread(path + "/images/input.jpg")

cv2.imshow('Hello World', input_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Getting Length and Height
print("Height of the image is",input_image.shape[0],"pixels")
print("Length of the image is",input_image.shape[1],"pixels")

#Saving images we modify
r = cv2.imwrite(path + '/images/output.jpg',input_image)
print("Status of writting image:",r)