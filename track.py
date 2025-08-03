import cv2
import mediapipe as mp
import serial

arduino = serial.Serial('COM5', 9600)


mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh()

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(img_rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
           
            nose = face_landmarks.landmark[1]
            x = int(nose.x * 100)  

            angle = int((x / 100) * 180)
            angle = max(0, min(180, angle))  

            arduino.write(f"{angle}\n".encode())

    cv2.imshow("Camera", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()
