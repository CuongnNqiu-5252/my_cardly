from pydantic import BaseModel, EmailStr, Field


class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(...,
                          min_length=8,
                          )


class UserLogin(BaseModel):
    email: str
    password: str
    def serializable_dict(self) -> dict:
        return {"email": self.email, "password": self.password}

class Token(BaseModel):
    access_token: str
    token_type: str
class UserResponse(BaseModel):
    username: str
    email: EmailStr
class UserUpdate(BaseModel):
    username: str
    email: EmailStr
    password: str
    def serializable_dict(self) -> dict:
        return {"username": self.username, "email": self.email, "password": self.password}

class RegisterResponse(BaseModel):
    username: str
    email: EmailStr