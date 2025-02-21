# 🚀 FastAPI User Management System

This is a **User Management API** built with **FastAPI, SQLAlchemy, and PostgreSQL**. The API allows you to **create, read, and delete users**, following best practices such as **data validation with Pydantic**, **database session management**, and **dependency injection**.

---

## 📌 Features
✅ **CRUD Operations** – Create, Read, and Delete users  
✅ **Database Integration** – PostgreSQL with SQLAlchemy ORM  
✅ **Pydantic Validation** – Ensures proper data validation  
✅ **Dependency Injection** – Efficient database session management  
✅ **Exception Handling** – Returns meaningful error messages  
✅ **Modular Structure** – Organized codebase for maintainability  

---

## 🛠️ Setup & Installation

### **1. Clone the Repository**
```bash
git clone https://github.com/gideon877/fastapi-user-management.git
cd fastapi-user-management
```

### **2. Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### **3. Install Required Packages**
```bash
pip install fastapi uvicorn sqlalchemy databases pydantic psycopg psycopg2-binary python-dotenv
```

### **4. Set Up Environment Variables**
Create a `.env` file and add your PostgreSQL database URL:
```env
DATABASE_URL=postgresql://username:password@localhost/dbname
```

### **5. Run the API**
```bash
uvicorn main:app --reload
```

---

## 📂 Project Structure
```
📂 fastapi-user-management
 ┣ 📜 main.py          # FastAPI app with API endpoints
 ┣ 📜 model.py         # SQLAlchemy database models
 ┣ 📜 schema.py        # Pydantic schemas for validation
 ┣ 📜 services.py      # Business logic and database operations
 ┣ 📜 database.py      # Database connection and session management
 ┣ 📜 .env             # Environment variables
 ┗ 📜 README.md        # API Documentation
```

---

## 🚀 API Endpoints

### **1️⃣ Create a New User**
**POST** `/users/`  
Creates a new user.

**Request Body (JSON)**  
```json
{
  "first_name": "John",
  "last_name": "Doe",
  "age": 25,
  "gender": "Male",
  "race": "Caucasian"
}
```

**Response**  
```json
{
  "id": 1,
  "first_name": "John",
  "last_name": "Doe",
  "age": 25,
  "gender": "Male",
  "race": "Caucasian"
}
```

---

### **2️⃣ Get All Users**
**GET** `/users/`  
Fetches a paginated list of users.

**Query Parameters**  
- `skip` (default: `0`) → Number of records to skip  
- `limit` (default: `10`) → Number of records to return  

**Response**  
```json
[
  {
    "id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "age": 25,
    "gender": "Male",
    "race": "Caucasian"
  },
  {
    "id": 2,
    "first_name": "Jane",
    "last_name": "Smith",
    "age": 30,
    "gender": "Female",
    "race": "Asian"
  }
]
```

---

### **3️⃣ Get a User by ID**
**GET** `/users/{user_id}`  
Fetches details of a single user.

**Example Request:**  
```
GET /users/1
```

**Response:**  
```json
{
  "id": 1,
  "first_name": "John",
  "last_name": "Doe",
  "age": 25,
  "gender": "Male",
  "race": "Caucasian"
}
```

**Error Response:**  
```json
{
  "detail": "User not found"
}
```

---

### **4️⃣ Delete a User**
**DELETE** `/users/{user_id}`  
Deletes a user by ID.

**Example Request:**  
```
DELETE /users/1
```

**Response:**  
```json
{
  "message": "User deleted successfully"
}
```

**Error Response:**  
```json
{
  "detail": "User not found"
}
```

---

## 📌 Future Enhancements
✅ Add filters and statistics (e.g., most common names, average age)  
✅ Implement user **update functionality**  
✅ Add **authentication and authorization**  

---

## ❤️ Contributing
Feel free to open issues and submit pull requests. Let's build something great together!

---

## 📜 License
This project is licensed under the **MIT License**.