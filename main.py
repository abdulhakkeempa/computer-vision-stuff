import cv2 as cv
import numpy as np

img = np.zeros((512,512,3),np.uint8)
# img[10:300,250:300] = 255,0,255

cv.line(img,(0,0),(512,512),(0,255,255),5)
cv.line(img,(0,512),(512,0),(0,255,255),5)
print(img.shape)
cv.rectangle(img,(10,10),(250,350),(255,0,255),cv.FILLED)
cv.circle(img,(256,256),100,(255,255,0),cv.FILLED)
cv.putText(img,"OPEN CV",(100,100),cv.FONT_HERSHEY_COMPLEX,2,(0,100,0),2)

cv.imshow('Image',img)
cv.waitKey(0)