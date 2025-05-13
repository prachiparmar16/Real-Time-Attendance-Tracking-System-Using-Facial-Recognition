# Real-Time-Attendance-Tracking-System-Using-Facial-Recognition
Thanks, Prachi! Now that I have both your files — `addToDatabase.py` (which initializes Firebase with student data) and `encoder.py` (which encodes face images and uploads them to Firebase Storage) — here is your **final, updated `README.md`** content for GitHub, accurately reflecting the full flow of your project:

---

# 🎓 Real-Time Attendance Tracking System Using Facial Recognition

# 📌 Project Overview

This project is a **Real-Time Attendance Tracking System** powered by **facial recognition** to automate attendance logging. It integrates **OpenCV**, **face\_recognition**, **Firebase Realtime Database**, and **Cloud Storage** to provide a seamless and contactless attendance solution. Designed for classrooms or organizations, it recognizes faces in real-time and updates attendance with timestamped records securely stored in Firebase.

## 🚀 Features

* 👤 Detects and recognizes faces using a webcam
* 🔄 Real-time attendance marking with visual feedback
* ☁️ Integrates with Firebase Realtime Database and Cloud Storage
* 🧠 Face encodings generated from training images
* 🖼️ Custom GUI using `cvzone` with mode switching (e.g., scanning, recognized, error)
* 📊 Displays student data like name, subject, semester, and attendance count
* 🔐 Ensures each student can only be marked present once in a time window

## 🛠️ Technologies Used

* **Python**
* **OpenCV** – for video capture and image processing
* **face\_recognition** – for facial encodings and comparisons
* **Firebase** – for real-time database and image storage
* **cvzone** – for easy UI overlay (e.g., corner rectangles)
* **NumPy**, **Pickle** – for encoding data handling

## 📂 Project Structure

```
├── main.py                # Main app: real-time recognition & attendance marking
├── encoder.py             # Encode student images and upload to Firebase Storage
├── addToDatabase.py       # Push static student details to Firebase Realtime DB
├── EncodeFile.p           # Pickled file with known encodings and student IDs
├── Images/                # Folder containing registered student face images
├── Resources/
│   ├── background.png     # Main background image
│   └── Modes/             # Visual feedback modes (e.g., recognized, error)
├── serviceAccountKey.json # Firebase credentials
└── README.md              # Project documentation
```

## 🔄 Workflow

### 1. Register Students (One-time setup)

* Store face images in `Images/` folder (filename = student ID).
* Run `encoder.py` to:

  * Encode faces
  * Upload images to Firebase Cloud Storage
  * Save encodings and IDs in `EncodeFile.p`

### 2. Add Student Details to Firebase

* Run `addToDatabase.py` to:

  * Populate student records (name, ID, subject, attendance count, etc.) in Firebase Realtime Database

### 3. Real-Time Attendance

* Run `main.py`:

  * Loads encodings from `EncodeFile.p`
  * Captures webcam feed
  * Detects and matches faces
  * Marks attendance in Firebase and displays student info with GUI

## 📝 Prerequisites

* Python 3.x
* Firebase Project:

  * Realtime Database & Cloud Storage enabled
  * Download `serviceAccountKey.json`
* Required packages:

  ```bash
  pip install opencv-python face_recognition firebase-admin cvzone numpy
  ```

## 💡 Future Enhancements

* Admin panel to manage students and attendance logs
* Web-based dashboard for analytics
* Mobile app for real-time view
* OTP/email confirmation on attendance



