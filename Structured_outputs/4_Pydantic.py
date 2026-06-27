from pydantic import BaseModel, Field , EmailStr
from typing import Optional

class Student(BaseModel):
    name: str = "Saksham"
    age: Optional[int] = None  # age is optional; if not provided, it defaults to None
    email : EmailStr
    cgpa: float = Field(
        gt=0,
        lt=10,
        default=5.0,
        description="Current CGPA"
    )

new_student = {
    "name": "Prasoon",
    "age": "21",
    "email":"abc@gmail.com",
    "cgpa": 8.1
}

student = Student(**new_student)

print(student)