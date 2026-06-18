# 🎯 YOLO Object Tracker with 80 COCO Classes

YOLO Object Tracker is a real-time computer vision application built using **Python 🐍, OpenCV 🎥, YOLOv8 🤖, and ByteTrack 🚀**.

The system detects and tracks objects from a live webcam feed, assigning a unique ID to each detected object while maintaining tracking across frames. Using the YOLOv8 COCO model, it can recognize up to **80 different object classes** in real time.

---

# ✨ Features

🎯 Real-Time Object Detection

* Detects objects directly from webcam feed

🆔 Multi-Object Tracking

* Assigns unique tracking IDs

🤖 YOLOv8 Powered

* Uses the powerful YOLOv8n model

📦 80 COCO Classes

* Person
* Car
* Bicycle
* Dog
* Cat
* Laptop
* Phone
* And many more...

🚀 ByteTrack Integration

* Smooth and accurate object tracking

📷 Live Webcam Support

* Works with any connected webcam

⚡ Auto Dependency Installation

* Automatically installs required packages

🖥 Lightweight Interface

* Simple OpenCV display window

---

# 📂 Project Structure

```text id="y7k3a2"
object-tracker-with-80-YOLO-model/
│
├── object tracker with 80 YOLO model.py
├── yolov8n.pt
├── README.md
└── LICENSE
```

---

# ⚙️ Installation

## 1️⃣ Clone the Repository

```bash id="w9m2k7"
git clone https://github.com/rsamwilson2323-cloud/object-tracker-with-80-YOLO-model.git

cd object-tracker-with-80-YOLO-model
```

---

## 2️⃣ Install Dependencies

The script automatically installs required packages.

Or install manually:

```bash id="v4n8p1"
pip install ultralytics opencv-python numpy torch torchvision
```

---

# 📦 Requirements

```text id="p2x6d9"
ultralytics
opencv-python
numpy
torch
torchvision
```

---

# ▶️ Usage

Run the program:

```bash id="f8q1r5"
python "object tracker with 80 YOLO model.py"
```

The webcam will start automatically.

To stop the program:

```text id="g3m7c1"
Press ENTER
```

---

# 🧠 How It Works

📷 Webcam Capture

Captures live video frames using OpenCV.

🤖 Object Detection

YOLOv8 identifies objects within each frame.

🆔 Object Tracking

ByteTrack assigns persistent IDs to detected objects.

📦 Class Recognition

Recognizes objects from the COCO dataset.

🖥 Visualization

Displays bounding boxes, class names, and tracking IDs.

---

# 📸 Example Output

```text id="n5t8r4"
ID 1 : person
ID 2 : laptop
ID 3 : cell phone
ID 4 : chair
```

---

# 🎯 Supported Object Categories

The YOLOv8 COCO model can detect up to 80 object types including:

* Person
* Car
* Truck
* Bus
* Bicycle
* Motorcycle
* Dog
* Cat
* Bird
* Laptop
* Keyboard
* Mouse
* Cell Phone
* TV
* Chair
* Bottle

And many more.

---

# 🚀 Future Improvements

📊 Object Counting

📈 Tracking Analytics

🔔 Motion Alerts

📹 Video Recording

🌐 IP Camera Support

🧠 Custom YOLO Models

☁ Cloud Integration

---

# 🎯 Learning Concepts

* Computer Vision
* Object Detection
* Object Tracking
* YOLOv8
* Deep Learning
* OpenCV
* Artificial Intelligence

---

# ⚠️ Disclaimer

This project is intended for educational, research, and learning purposes only.

Performance depends on camera quality, lighting conditions, and hardware specifications.

---

# 👨‍💻 Author

**R. Sam Wilson**

🌐 GitHub

https://github.com/rsamwilson2323-cloud

💼 LinkedIn

https://www.linkedin.com/in/sam-wilson-14b554385

---

# 📜 License

This project is licensed under the MIT License.
