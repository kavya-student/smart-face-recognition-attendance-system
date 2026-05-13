🤖🎓 Smart Face Recognition Attendance System 🧠📸📝
A Smart Face Recognition Attendance System built using 🐍 Python, 📷 OpenCV, 
and 🧠 MediaPipe. The project detects and recognizes faces in real time, verifies that the 
person is live through 👁️ blink detection, and automatically records attendance in a 📄 CSV file.

🚀✨ Features
📷 Real-time face detection using OpenCV
🧠 Face recognition using LBPH Face Recognizer
👁️ Blink-based liveness detection using MediaPipe Face Mesh
📝 Automatic attendance marking with 📅 date and ⏰ time
👥 Support for multiple users
📄 CSV-based attendance storage
🔒 Anti-spoof protection against photos

🛠️💻 Technologies Used
🐍 Python
📷 OpenCV
🧠 MediaPipe
🔢 NumPy
🖼️ Pillow

📁🗂️ Project Structure
smart-face-recognition-attendance-system/
│── dataset_creator.py
│── trainer.py
│── recognizer.py
│── liveness_check.py
│── main_attendance.py
│── labels.txt
│── requirements.txt
│── README.md
│── .gitignore
│
├── dataset/        # 📸 Generated face images (not uploaded)
├── trainer/        # 🧠 Generated trained model (not uploaded)
└── attendance.csv  # 📝 Generated attendance log (not uploaded)

⚙️🔧 Installation
1️⃣ Clone the Repository
git clone https://github.com/kavya-student/smart-face-recognition-attendance-system.git
cd smart-face-recognition-attendance-system

2️⃣ Install Dependencies
pip install -r requirements.txt

▶️🚀 How to Run
📸 1. Capture Face Dataset
python dataset_creator.py

This captures face images and stores them in the dataset/ folder.

🧠 2. Train the Model
python trainer.py

This trains the LBPH recognizer and saves the model in trainer/trainer.yml.

📝 3. Start Smart Attendance System
python main_attendance.py

The system will:
👤 Detect and recognize faces
👁️ Perform blink-based liveness detection
✅ Verify the user is real
📝 Record attendance in attendance.csv

📄📂 Output Files
📸 dataset/ → Captured face images
🧠 trainer/trainer.yml → Trained face recognition model
🏷️ labels.txt → Mapping between IDs and names
📝 attendance.csv → Attendance records with date and time

💼🎯 Use Cases
🏫 Classroom attendance
🏢 Office attendance
🔐 Secure access systems
🤖 Computer vision learning projects
🎓 Academic mini and major projects

🔮🚀 Future Enhancements
🖥️ Graphical User Interface (GUI)
🗄️ Database integration (MySQL)
📧 Email notifications
🌐 Web dashboard using Flask
☁️ Cloud deployment

👩‍💻🌟 Author
Kavya Sharma 💖

📜📘 License
This project is created for 🎓 educational and 💼 portfolio purposes.
