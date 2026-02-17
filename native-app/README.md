# 👁️ Eye-Cursor

An innovative eye-tracking-based cursor control system built across multiple platforms — mobile, web and backend services.  
This project enables users to interact with devices using eye movements, combining **React Native**, **web frontend**, and a powerful **backend API**.

---

## 🧠 What Is Eye-Cursor?

Eye-Cursor is a cross-platform project that tracks eye movement using device cameras and translates this into cursor interactions and user actions.  
With this system, you can:

✨ Move the cursor using eye gaze  
✨ Click or interact via eye patterns  
✨ Use it on Android & iOS (via React Native)  
✨ Access a web frontend interface  
✨ Connect to backend APIs for extended functionality

---

## 📁 Project Structure

eye-cursor/
├── backend/ # Server / API logic
├── frontend/ # Web application (UI & interactions)
├── native-app/ # React Native app for mobile
├── .gitignore
├── requirements.txt
└── README.md

Each folder encapsulates a core part of the system:

- **backend/** – APIs to handle eye-tracking data and logic  
- **frontend/** – Browser-based UI for visual feedback & controls  
- **native-app/** – Mobile app built using React Native for eye tracking support

---

## 🚀 Getting Started

### 🧩 Prerequisites

Ensure you have the following installed:

- Node.js & npm (or yarn)
- React Native CLI or Expo (based on project setup)
- Android Studio / Xcode (for mobile testing)
- Python if backend uses it)
- Git

---

## 📲 Setup — Mobile (React Native)

```bash
cd native-app
# install dependencies
npm install
# run app (Android)
npx react-native run-android
# or run app (iOS)
npx react-native run-ios
```

🌐 Setup — Web Frontend
cd frontend
npm install
npm start

🛠️ Setup — Backend (Python)
📌 Prerequisites

Python 3.9+

pip

Virtual environment (recommended)

🔹 Step 1 — Navigate to backend folder
cd backend

🔹 Step 2 — Create Virtual Environment (Recommended)
python -m venv venv
Activate it:

Windows
venv\Scripts\activate
Mac/Linux
source venv/bin/activate

🔹 Step 3 — Install Dependencies
pip install -r requirements.txt

🔹 Step 4 — Run Backend Server
uvicorn main:app --reload
