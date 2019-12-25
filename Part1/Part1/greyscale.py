
import cv2
import numpy as np
global path

path = "C:/Users/Ryan/source/repos/OpenCVTutorial"
img = cv2.imread(path + "/images/input.jpg") #can use img = cv2.imread(path,0) to greyscale the image automatically
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Converting the colors of the image

cv2.imshow('Greyscaled',gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()


hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #Convert the RGB to HSV colors
cv2.imshow("HSV image",hsv_img)
cv2.imshow("Hue Channel",hsv_img[:, :, 0])
cv2.imshow("Saturation Channel",hsv_img[:, :, 1])
cv2.imshow("Value Channel",hsv_img[:, :, 2])

cv2.waitKey(0)
cv2.destroyAllWindows()

#Now splitting the image into RGB


zeros = np.zeros(img.shape[:2], dtype="uint8")

B, G, R = cv2.split(img)

cv2.imshow("Blue",cv2.merge([B,zeros,zeros]))
cv2.imshow("Green",cv2.merge([zeros,G,zeros]))
cv2.imshow("Red",cv2.merge([zeros,zeros,R]))

cv2.waitKey(0)
cv2.destroyAllWindows()

#Merging the colors again

merged = cv2.merge([B,G,R])
cv2.imshow("Merged",merged)

merged_blueAmp = cv2.merge([B+50,G,R])
cv2.imshow("Merged, blue boost", merged_blueAmp)

cv2.waitKey(0)
cv2.destroyAllWindows()