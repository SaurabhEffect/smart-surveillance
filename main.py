import cv2
import time
import os
import sounddevice as sd
import numpy as np

def play_alert_sound():
    fs = 44100  # Sample rate
    duration = 1.0  # seconds
    frequency = 1000  # 1000 Hz beep

    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    sound_wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    sd.play(sound_wave, fs)
    sd.wait()

face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

if not os.path.exists("intruders"):
    os.mkdir("intruders")

cap = cv2.VideoCapture(0)
time.sleep(2)
first_frame = None
img_counter = 0

while True:
    check, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if len(faces) > 0:
        play_alert_sound()

        img_name = f"intruders/face_intruder_{time.strftime('%Y%m%d_%H%M%S')}.png"
        cv2.imwrite(img_name, frame)
        print(f"[ALERT] Face detected & saved: {img_name}")
        time.sleep(1)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    contours, _ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        img_name = f"intruders/intruder_{time.strftime('%Y%m%d_%H%M%S')}.png"
        cv2.imwrite(img_name, frame)
        print(f"🔔 Intruder detected! Image saved as {img_name}")
        time.sleep(1)

    cv2.imshow("Smart Surveillance", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

