# Student Management System

A backend-focused Student Management System built with Python and FastAPI. The project provides RESTful APIs for managing student records with CRUD operations, validation, searching, filtering, and pagination.

This project is being developed as a practical backend project to improve skills in Python, FastAPI, REST APIs, SQLAlchemy, database management, and backend architecture.

## 🚀 Features

- Create student records
- Get all students
- Get student by ID
- Update student details
- Delete student records
- Search students by name
- Filter students by course
- Pagination for student records
- Email validation
- Duplicate email handling
- Proper HTTP error handling
- Pydantic request and response validation
- Interactive API documentation with Swagger UI
- SQLite database integration
- SQLAlchemy ORM

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- Pydantic

### Database
- SQLite

### API Documentation
- Swagger UI
- OpenAPI

### Development Tools
- Git
- GitHub
- VS Code
- Uvicorn

## 📁 Project Structure

```text
Student-Management-System/
│
├── app/
│   ├── main.py
│   ├── database.py
│   │
│   ├── models/
│   │   ├── student.py
│   │   └── user.py
│   │
│   ├── schemas/
│   │   ├── student.py
│   │   └── user.py
│   │
│   ├── routes/
│   │   ├── students.py
│   │   └── auth.py
│   │
│   └── services/
│       └── auth.py
│
├── .gitignore
├── requirements.txt
└── README.md