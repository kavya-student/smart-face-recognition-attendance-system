import cv2
import csv
from datetime import datetime
import mediapipe as mp
labels = {}
with open("labels.txt", "r") as f:
    for line in f:
        id, name = line.strip().split(",")
        labels[int(id)] = name

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer/trainer.yml")


face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)


blink_count = 0
blink_detected = False
attendance_marked = set()

LEFT_EYE_TOP = 159
LEFT_EYE_BOTTOM = 145

def mark_attendance(name):
    filename = "attendance.csv"
    now = datetime.now()
    time_string = now.strftime("%H:%M:%S")
    date_string = now.strftime("%Y-%m-%d")

    if name not in attendance_marked:
        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([name, date_string, time_string])

        attendance_marked.add(name)
        print(f"{name} attendance marked")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)


    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    results = face_mesh.process(rgb)

    for (x, y, w, h) in faces:
        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        if confidence < 50:
            name = labels.get(id, "Unknown")
        else:
            name = "Unknown"

        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(
            frame,
            name,
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )

        # Blink detection
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                top = face_landmarks.landmark[LEFT_EYE_TOP]
                bottom = face_landmarks.landmark[LEFT_EYE_BOTTOM]

                top_y = int(top.y * frame.shape[0])
                bottom_y = int(bottom.y * frame.shape[0])

                eye_distance = abs(top_y - bottom_y)

                if eye_distance < 5:
                    blink_detected = True
                elif blink_detected:
                    blink_count += 1
                    blink_detected = False

                cv2.putText(
                    frame,
                    f"Blinks: {blink_count}",
                    (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2
                )

                if blink_count >= 1 and name != "Unknown":
                    cv2.putText(
                        frame,
                        "REAL VERIFIED",
                        (30, 100),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1,
                        (0, 255, 0),
                        2
                    )
                    mark_attendance(name)

    cv2.imshow("Smart Attendance", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()