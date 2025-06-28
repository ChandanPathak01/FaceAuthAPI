# 🔐 FaceVerify – Face Recognition Authentication API

**FaceVerify** is a secure, FastAPI-based web application that allows user registration with facial image data and provides face matching to verify user identity. It is ideal for scenarios like entry validation, attendance systems, and Aadhaar-based user verification.

## 🛠️ Tech Stack

- **Language:** Python 3.9
- **Framework:** FastAPI
- **ORM:** SQLAlchemy
- **Validation:** Pydantic
- **Authentication:** JOSE (JWT)
- **Face Recognition:** `face_recognition` (uses dlib)
- **Database:** PostgreSQL
- **Frontend:** HTML + JavaScript (one-page UI)
- **Others:** OpenCV, PIL, Python-Multipart

## 🚀 Features

- ✅ Register a user with Aadhaar number, contact info, and face image
- ✅ Extract and store face encodings
- ✅ Upload another photo to check match percentage
- ✅ Secure endpoints using JWT tokens
- ✅ Simple one-page web interface
- ✅ Fast, reliable API for real-time face comparison


## 📂 Project Structure

FaceVerify/
├── backend/
│ ├── main.py # FastAPI app entrypoint
│ ├── database.py # PostgreSQL database setup
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic models for validation
│ ├── auth.py # JWT token generation and verification
│ ├── utils.py # Face encoding and matching logic
│ └── routers/
│ ├── register.py # User registration API
│ └── match.py # Face matching API
├── frontend/
│ └── index.html # Simple HTML UI for register and match
├── requirements.txt
└── README.md

## 🧰 Installation
### ✅ Prerequisites

- Python 3.9
- PostgreSQL (running locally or in Docker)
- Virtual environment (recommended)

### ⚙️ Steps

# Clone the repo
git clone https://github.com/your-username/FaceVerify.git
cd FaceVerify

# Create a virtual environment
python -m venv venv
venv\Scripts\activate  # For Windows
# source venv/bin/activate  # For Linux/macOS

# Install dependencies
pip install -r requirements.txt

🗃️ PostgreSQL Configuration
Ensure PostgreSQL is running and accessible.
Update the default connection string if needed in backend/database.py:
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

🏃 Run the App
# From the backend directory
cd backend
uvicorn main:app --reload
Visit: http://127.0.0.1:8000/docs for Swagger UI
Open frontend/index.html in your browser to use the UI

📦 API Endpoints
POST /register: Register a user with Aadhaar and photo
POST /match: Upload another photo to verify identity
POST /login: Login using Aadhaar
GET /users: Get all registered users (JWT protected)

✅ Example Use Case
Admin registers a user with their Aadhaar and photo
Later, the user uploads a different photo
System checks the face and gives match percentage
If match > threshold (e.g., 85%), allow access

🔒 Authentication
This project uses JWT (via python-jose) to protect sensitive endpoints.
🧪 Testing (optional)
Testing can be done using pytest. Write unit tests for API routes and face matching functions.
📜 License
MIT License — free to use, modify, and distribute.

🙋‍♂️ Author
Chandan Pathak
📧 chandanpathak616@gmail.com
📱 +91-8210195043
🌐 GitHub: @your-username

🌟 Show Your Support
If you like this project, ⭐️ it on GitHub and share it with others!
