#FACE DETECTION

import cv2

har_cass = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
imp_img = cv2.VideoCapture("girl.jpg")

res,img = imp_img.read()

grey = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#grey = cv2.cvtColor(img, cv2.COLOR_RED)

face = har_cass.detectMultiScale(grey,2.3,6)

for (x,y,w,h) in face:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,255,0),2)

cv2.imshow("Elon pic", img)

cv2.waitKey(0)
imp_img.release()
cv2.destroyAllWindows()
