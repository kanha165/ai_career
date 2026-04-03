from pydantic import BaseModel, EmailStr

from pydantic import BaseModel, EmailStr, field_validator
import re

class UserSignup(BaseModel):
    name: str
    email: EmailStr
    password: str

    @field_validator("password")
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters")

        if not re.search(r"[A-Z]", value):
            raise ValueError("Password must contain uppercase letter")

        if not re.search(r"[a-z]", value):
            raise ValueError("Password must contain lowercase letter")

        if not re.search(r"[0-9]", value):
            raise ValueError("Password must contain number")

        if not re.search(r"[!@#$%^&*]", value):
            raise ValueError("Password must contain special character")

        return value

class UserLogin(BaseModel):
    email: EmailStr
    password: str
    

class ResetPasswordSchema(BaseModel):
    email: str
    otp: str
    new_password: str

    @field_validator("new_password")
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters")

        if not re.search(r"[A-Z]", value):
            raise ValueError("Must contain 1 uppercase letter")

        if not re.search(r"[a-z]", value):
            raise ValueError("Must contain 1 lowercase letter")

        if not re.search(r"[0-9]", value):
            raise ValueError("Must contain 1 number")

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise ValueError("Must contain 1 special character")

        return value    