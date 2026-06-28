from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class Student(BaseModel):
    name: str = "Saksham"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(
        gt=0,
        lt=10,
        default=5.0,
        description="Current CGPA"
    )

new_student = {
    "name": "Prasoon",
    "age": "21",
    "email": "abc@gmail.com",
    "cgpa": 8.1
}

student = Student(**new_student)

print(student)

# Convert to Dictionary
student_dict = student.model_dump()

print(student_dict)
print(student_dict["age"])

# Convert to JSON
student_json = student.model_dump_json()

print(student_json)