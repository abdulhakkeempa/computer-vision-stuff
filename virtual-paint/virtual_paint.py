import cv2 as cv

print("Hi")
frameWidth = 640
frameHeight = 480
cap = cv.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(3,frameHeight)
cap.set(10,130)

while True:
    success,img = cap.read()
    cv.imshow("Result",img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        print('q pressed')
        cv.destroyAllWindows()
        break