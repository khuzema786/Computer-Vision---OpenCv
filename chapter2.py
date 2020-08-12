# BASIC FUNCTIONS

import cv2
import numpy as np

img = cv2.imread("Resources/lena.png")
# 5x5 Identity Matrix, with object type as unsigned int i.e, 0-255
kernel = np.ones((5, 5), np.uint8)

# Converts the image in different color spaces
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Gray scaled image
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)  # Blurred image
imgCanny = cv2.Canny(img, 150, 200)  # Edge selection
# Edge Thickening, Increasing Iteration increases thickness
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)  # Edge thinning

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dialation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)

print("Code Completed")
