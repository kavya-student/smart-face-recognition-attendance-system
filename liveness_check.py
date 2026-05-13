import cv2
import mediapipe as mp
import time

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(refine_landmarks=True)

cap = cv2.VideoCapture(0)

blink_count = 0
blink_detected = False

LEFT_EYE_TOP = 159
LEFT_EYE_BOTTOM = 145

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            h, w, _ = frame.shape

            top = face_landmarks.landmark[LEFT_EYE_TOP]
            bottom = face_landmarks.landmark[LEFT_EYE_BOTTOM]

            top_y = int(top.y * h)
            bottom_y = int(bottom.y * h)

            eye_distance = abs(top_y - bottom_y)

            if eye_distance < 5:
                blink_detected = True
            elif blink_detected:
                blink_count += 1
                blink_detected = False

            cv2.putText(frame, f"Blinks: {blink_count}", (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            if blink_count >= 1:
                cv2.putText(frame, "REAL PERSON VERIFIED", (30, 100),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Liveness Check", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()