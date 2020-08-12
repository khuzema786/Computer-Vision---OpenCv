# # Color Detection Using Webcam

# import cv2
# import numpy as np

# frameWidth = 640
# frameHeight = 480
# cap = cv2.VideoCapture(0)
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)
# frameCounter = 0


# def empty(a):
#     pass


# cv2.namedWindow("HSV")  # Creating a new window
# cv2.resizeWindow("HSV", 640, 240)  # Size of new window
# # New window contains HSV trackbars
# cv2.createTrackbar("HUE Min", "HSV", 0, 179, empty)
# cv2.createTrackbar("HUE Max", "HSV", 179, 179, empty)
# cv2.createTrackbar("SAT Min", "HSV", 0, 255, empty)
# cv2.createTrackbar("SAT Max", "HSV", 255, 255, empty)
# cv2.createTrackbar("VALUE Min", "HSV", 0, 255, empty)
# cv2.createTrackbar("VALUE Max", "HSV", 255, 255, empty)


# while True:
#     frameCounter += 1
#     if cap.get(cv2.CAP_PROP_FRAME_COUNT) == frameCounter:
#         cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
#         frameCounter = 0

#     _, img = cap.read()
#     imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#     h_min = cv2.getTrackbarPos("HUE Min", "HSV")
#     h_max = cv2.getTrackbarPos("HUE Max", "HSV")
#     s_min = cv2.getTrackbarPos("SAT Min", "HSV")
#     s_max = cv2.getTrackbarPos("SAT Max", "HSV")
#     v_min = cv2.getTrackbarPos("VALUE Min", "HSV")
#     v_max = cv2.getTrackbarPos("VALUE Max", "HSV")
#     print(h_min)

#     lower = np.array([h_min, s_min, v_min])
#     upper = np.array([h_max, s_max, v_max])
#     mask = cv2.inRange(imgHsv, lower, upper)
#     # Create a new image from mask & original image
#     result = cv2.bitwise_and(img, img, mask=mask)

#     mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
#     hStack = np.hstack([img, mask, result])
#     cv2.imshow('Horizontal Stacking', hStack)
#     if cv2.waitKey(1) and 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

# Color Detection Using Image
import cv2
import numpy as np


def empty(a):
    pass


def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(
                        imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(
                        imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(
                        imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(
                    imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(
                    imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


path = 'Resources/lambo.png'
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 19, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 110, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 240, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 153, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min, h_max, s_min, s_max, v_min, v_max)
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    # cv2.imshow("Original",img)
    # cv2.imshow("HSV",imgHSV)
    # cv2.imshow("Mask", mask)
    # cv2.imshow("Result", imgResult)

    imgStack = stackImages(0.6, ([img, imgHSV], [mask, imgResult]))
    cv2.imshow("Stacked Images", imgStack)
    cv2.waitKey(1)
