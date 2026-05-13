import cv2
import os
import time

name = "kavya"  
dataset_path = "dataset"

if not os.path.exists(dataset_path):
    os.makedirs(dataset_path)

cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

count = 0

print("Look at camera and move slightly...")

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        count += 1

        cv2.imwrite(f"{dataset_path}/User.{name}.{count}.jpg", face)
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)

        time.sleep(0.2) 

    cv2.imshow("Capturing", img)

    if cv2.waitKey(1) == 27 or count >= 100:
        break

cam.release()
cv2.destroyAllWindows()