import cv2
import numpy as np
from datetime import datetime
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer/trainer.yml")
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
id_to_name = {}
with open("labels.txt", "r") as f:
    for line in f:
        id, name = line.strip().split(",")
        id_to_name[int(id)] = name

cam = cv2.VideoCapture(0)
marked_names = set()  
while True:
    ret, img = cam.read()
    if not ret:
        break
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
        if confidence < 60:
            name = id_to_name.get(id, "Unknown")
        else:
            name = "Unknown"
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(img, f"{name} ({round(confidence,1)})",
                    (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (255, 255, 255), 2)

        if name != "Unknown" and name not in marked_names:
            marked_names.add(name)
            with open("attendance.csv", "a") as f:
                now = datetime.now()
                date = now.strftime("%Y-%m-%d")
                time = now.strftime("%H:%M:%S")
                f.write(f"{name},{date},{time}\n")

    cv2.imshow("Face Recognition Attendance", img)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()