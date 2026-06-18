# =========================================================
# AUTO INSTALL + YOLO OBJECT TRACKING
# EXIT ONLY WHEN ENTER KEY IS PRESSED
# =========================================================

import sys
import subprocess
import os

# ---------------- AUTO INSTALL ----------------
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

required_packages = [
    "ultralytics",
    "opencv-python",
    "numpy",
    "torch",
    "torchvision"
]

for pkg in required_packages:
    try:
        __import__(pkg.split("-")[0])
    except ImportError:
        print(f"[INSTALLING] {pkg}")
        install(pkg)

# ---------------- IMPORTS ----------------
import cv2
from ultralytics import YOLO

# ---------------- DOWNLOAD MODEL ----------------
MODEL_NAME = "yolov8n.pt"

if not os.path.exists(MODEL_NAME):
    print("[DOWNLOADING MODEL] yolov8n.pt")
    model = YOLO(MODEL_NAME)
else:
    model = YOLO(MODEL_NAME)

# ---------------- VIDEO CAPTURE ----------------
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Webcam not found")
    exit()

print("✅ Webcam started")
print("👉 Press ENTER to exit")

# ---------------- TRACKING LOOP ----------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.track(
        frame,
        persist=True,
        conf=0.4,
        iou=0.5,
        tracker="bytetrack.yaml"
    )

    if results and results[0].boxes.id is not None:
        boxes = results[0].boxes.xyxy.cpu().numpy()
        ids = results[0].boxes.id.cpu().numpy()
        classes = results[0].boxes.cls.cpu().numpy()

        for box, track_id, cls in zip(boxes, ids, classes):
            x1, y1, x2, y2 = map(int, box)
            label = model.names[int(cls)]

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            text = f"ID {int(track_id)} : {label}"
            cv2.putText(
                frame,
                text,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    cv2.imshow("YOLO Object Tracking", frame)

    # -------- EXIT ONLY ON ENTER --------
    key = cv2.waitKey(1)
    if key == 13:   # ENTER key ASCII
        print("⏹ ENTER pressed → exiting")
        break

# ---------------- CLEANUP ----------------
cap.release()
cv2.destroyAllWindows()
print("✅ Camera closed safely")
