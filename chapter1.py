import cv2

# ---- Read Image ----

# LOAD AN IMAGE USING 'IMREAD'
img = cv2.imread("Resources/lena.png")
# DISPLAY
cv2.imshow("Lena Soderberg", img)
cv2.waitKey(0)

# ---- Read Video ----

cap = cv2.VideoCapture("Resources/test_video.mp4")
while True:
    # success will be a boolean variable used for error handling
    success, img = cap.read()
    cv2.imshow("Result", img)
    # This key is automatically pressed after a delay of 1sec for the video frame to change
    key = cv2.waitKey(1)

    # Stop if Q key is pressed
    if key == 81 or key == 113:
        break

# ---- Read Webcam ----

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)  # For frame width the id is 3
cap.set(4, frameHeight)  # For frame height the id is 4
cap.set(10, 150)  # For brightness the id is 10
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    # This key is automatically pressed after a delay of 1sec for the video frame to change
    key = cv2.waitKey(1)

    # Stop if Q key is pressed
    if key == 81 or key == 113:
        break

print("Completed")
