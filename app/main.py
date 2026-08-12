from fastapi import FastAPI

from app.database import engine, Base
from app.models.student import Student
from app.routes.students import router as student_router

from app.models.user import User
from app.routes.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Student Management System")

app.include_router(student_router)
app.include_router(auth_router)


@app.get("/")
def home():
    return {"message": "Student Management System API is running"}