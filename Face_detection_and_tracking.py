import cv2

alg = "haarcascade_frontalface_default.xml"

haar_cascade = cv2.CascadeClassifier(alg) #loading

cam = cv2.VideoCapture(0)

while True:
    _,img = cam.read()
    

    grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    face = haar_cascade.detectMultiScale(grayimg,1.3,4)
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),5)
        cv2.imshow("Face Detection",img)
    
    key = cv2.waitKey(10)
    if key == 27:
        break
cam.release()
cv2.destroyAllWindows()