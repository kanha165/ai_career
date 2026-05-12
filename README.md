# 🚀 AI Career Path Recommendation System

An intelligent AI-based system that recommends **personalized career paths** and generates **step-by-step learning roadmaps** based on user skills and interests.

🔗 **Live Demo:**  
👉 https://ai-career-vk6r.onrender.com  

📂 **GitHub Repository:**  
👉 https://github.com/kanha165/ai_career  

---

## ✨ Features

- 🔐 Secure User Authentication (Register/Login)
- 🤖 AI-Based Career Prediction
- 🧠 Personalized Roadmap Generation
- 📊 Machine Learning Integration
- 🔒 JWT Protected Routes
- ⚡ FastAPI High Performance Backend
- 🌐 Interactive API Docs (Swagger UI)
---

## 🛠️ Tech Stack

### 🔹 Backend
- FastAPI
- Python
- Uvicorn

### 🔹 Machine Learning
- Scikit-learn
- Pandas
- NumPy

### 🔹 Database
- PostgreSQL / SQLite
- SQLAlchemy

### 🔹 Authentication
- JWT (JSON Web Tokens)
- Passlib (bcrypt hashing)

---

## 📂 Project Structure

ai_career/
│
├── app/
│   ├── routes/
│   │   ├── auth.py
│   │   ├── predict.py
│   │   ├── roadmap.py
│   │   └── protected.py
│   │
│   ├── models/
│   ├── schemas/
│   ├── database.py
│   └── main.py
│
├── requirements.txt
├── README.md
└── .env

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
git clone https://github.com/kanha165/ai_career.git  
cd ai_career  

### 2️⃣ Create Virtual Environment
python -m venv venv  
venv\Scripts\activate     # Windows  
source venv/bin/activate  # Linux/Mac  

### 3️⃣ Install Dependencies
pip install -r requirements.txt  

---

## ▶️ Run Locally

uvicorn app.main:app --reload  

Open browser:  
http://127.0.0.1:8000/docs  

---

## 🔑 API Endpoints

### 🔐 Auth
- POST /auth/register → Register new user  
- POST /auth/login → Login user  

### 🤖 Prediction
- POST /predict → Predict career path  

### 🧠 Roadmap
- POST /roadmap → Generate learning roadmap  

### 🔒 Protected
- GET /protected → Requires JWT token  

---

## 🤖 How It Works

1. User enters skills & interests  
2. ML model analyzes input  
3. Best career path is predicted  
4. AI generates structured roadmap  
5. User receives personalized guidance  

---

## 📊 Example Input

{
  "skills": ["python", "problem solving", "math"],
  "interest": "AI"
}

---

## 📈 Example Output

{
  "career": "Machine Learning Engineer",
  "roadmap": [
    "Python",
    "Data Structures",
    "Machine Learning Basics",
    "Projects"
  ]
}

---

## 🔒 Security Features

- 🔐 Password hashing using bcrypt  
- 🛡️ JWT authentication  
- 🚫 Protected routes access control  

---

## 🚀 Deployment

Hosted on Render  
https://ai-career-vk6r.onrender.com  

---

## 🧠 Future Improvements

- 🎨 Frontend UI (React / HTML CSS)  
- 📄 Resume-based career prediction  
- 💬 AI Chatbot integration  
- ☁️ Advanced cloud deployment (AWS / Docker)  

---

## 👨‍💻 Author

Kanha Patidar  
B.Tech CSIT (IT)  
AI/ML Enthusiast  

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---

## 📜 License

This project is for educational purposes.
