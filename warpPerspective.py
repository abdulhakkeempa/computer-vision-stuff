import cv2 as cv
import numpy as np

img = cv.imread('img/cards.jpg')

WIDTH,HEIGHT = 418,552
points1 = np.float32([[516,138],[934,295],[310,690],[690,856]])
points2 = np.float32([[0,0],[WIDTH,0],[0,HEIGHT],[WIDTH,HEIGHT]])

matrix = cv.getPerspectiveTransform(points1,points2)
imgWrap = cv.warpPerspective(img,matrix,(WIDTH,HEIGHT))

cv.imshow("Original Image",img)
cv.imshow("Wrap Image",imgWrap)

cv.waitKey(0)