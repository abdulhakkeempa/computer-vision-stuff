import cv2 as cv
import numpy as np


def getContours(img):
    global imgContour
    contours,hierarchy = cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area>500:
            cv.drawContours(imgContour,cnt,-1,(255,0,255),2)
            peri = cv.arcLength(cnt,True)
            # print(peri)
            approx = cv.approxPolyDP(cnt,0.02*peri,True)
            # print(len(approx))
            objCor = len(approx)
            x,y,w,h = cv.boundingRect(approx)

            if objCor ==3:
                ObjectType = "Tri"
            elif objCor == 4:
                aspectRatio = w/float(h)
                if aspectRatio>0.95 and aspectRatio <1.05:
                    ObjectType = "Square"
                else:
                    ObjectType = "Rectangle"
            elif objCor == 5 :
                ObjectType = "Pentagon"
            else:
                ObjectType ="Cicle"
            cv.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0))
            cv.putText(imgContour,ObjectType,(x+(w//2)-10,y+(h//2)-10),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1)


img = cv.imread('img/shapes.jpg')
img = cv.resize(img,(img.shape[1]-400,img.shape[0]-400))
imgContour = img.copy()

imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgGray,(11,11),1)
imgCanny = cv.Canny(imgBlur,50,50)

# cv.imshow("Original Image",img)
# cv.imshow("Gray Image",imgGray)
# cv.imshow("Blur Image",imgBlur)
# cv.imshow("Canny Image",imgCanny)


getContours(imgCanny)
cv.imshow("Contour Image",imgContour)


cv.waitKey(0)