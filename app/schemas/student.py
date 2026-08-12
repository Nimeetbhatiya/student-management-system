from pydantic import BaseModel, ConfigDict, EmailStr


class StudentCreate(BaseModel):
    name: str
    email: EmailStr
    age: int
    course: str



class StudentUpdate(BaseModel):
    name: str
    email: EmailStr
    age: int
    course: str


class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: int
    course: str

    model_config = ConfigDict(from_attributes=True)