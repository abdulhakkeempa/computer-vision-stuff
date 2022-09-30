## Let Xplore - Saturday Hacknight TinkerHub 
### Open CV

#### Warp Perspective
```
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
```

![image](https://user-images.githubusercontent.com/92361680/193186443-1b539178-a9aa-4521-bd3b-671cc72133dd.png)


#### Face Detection Snippets
```
import cv2 as cv

faceCascade = cv.CascadeClassifier(f'{cv.data.haarcascades}haarcascade_frontalface_default.xml')

#add your image path containing faces.
path = ''

img = cv.imread(path)

#converting the image to gray scale
imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#extracting the images inside the input image using the trained model.
faces = faceCascade.detectMultiScale(imgGray,1.1,4)

#drawing an outing box over each shape.
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv.imshow("Image",img)
cv.waitKey(0)
```

### Shape Identifier Snippets
```
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
```
