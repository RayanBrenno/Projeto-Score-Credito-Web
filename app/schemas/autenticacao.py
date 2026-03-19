from pydantic import BaseModel, EmailStr

class RegisterSchema(BaseModel):
    name: str
    email: EmailStr
    password: str

class LoginSchema(BaseModel):
    email: EmailStr
    password: str

class UserResponseSchema(BaseModel):
    id: str
    name: str
    email: EmailStr

class TokenResponseSchema(BaseModel):
    access_token: str
    token_type: str
    user: UserResponseSchema