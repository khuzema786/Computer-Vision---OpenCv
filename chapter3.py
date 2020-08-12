# Crop and Resize
# ----------- X-Axis
# |
# |     .(w,h)
# |
# | Y-Axis

import cv2

img = cv2.imread("Resources/lambo.png")
print(img.shape)  # gives dimensions i.e, (height, width, color channel)

imgResize = cv2.resize(img, (1000, 500))  # (width, height)
print(imgResize.shape)

imgNotCropped = img[:]  # Display the entire image without cropping
imgCropped = img[0:200, 200:500]  # (height, width)

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Image Cropped", imgCropped)
cv2.imshow("Image Not Cropped", imgNotCropped)

cv2.waitKey(0)

print("Code Completed")
