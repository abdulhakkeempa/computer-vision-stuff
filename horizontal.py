import cv2 as cv
import numpy as np

def sample(a):
    pass

cv.namedWindow("TrackedBars")
cv.resizeWindow("TrackedBars",640,240)
cv.createTrackbar("Hue Min","TrackedBars",0,179,sample)
cv.createTrackbar("Hue Max","TrackedBars",179,179,sample)
cv.createTrackbar("Saturation Min","TrackedBars",0,255,sample)
cv.createTrackbar("Saturation Max","TrackedBars",255,255,sample)
cv.createTrackbar("Val Min","TrackedBars",0,221,sample)
cv.createTrackbar("Val Max","TrackedBars",221,221,sample)


while True:
    img = cv.imread("img/shapes.jpg")
    img = cv.resize(img,(img.shape[1]-200,img.shape[0]-200))
    hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    h_min = cv.getTrackbarPos("Hue Min","TrackedBars")
    h_max = cv.getTrackbarPos("Hue Max","TrackedBars")
    s_min = cv.getTrackbarPos("Saturation Min","TrackedBars")
    s_max = cv.getTrackbarPos("Saturation Max","TrackedBars")
    v_min = cv.getTrackbarPos("Val Min","TrackedBars")
    v_max = cv.getTrackbarPos("Val Max","TrackedBars")
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv.inRange(hsv,lower,upper)
    imgResult = cv.bitwise_and(img,img,mask=mask)

    cv.imshow("Color",img)
    cv.imshow("HSV",hsv)
    cv.imshow("Mask",mask)
    cv.imshow("Image Result",imgResult)


    cv.waitKey(1)
