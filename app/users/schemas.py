from datetime import date

from pydantic import BaseModel, EmailStr


class SUserCreate(BaseModel):
    email: EmailStr
    password: str


class SUserAuth(BaseModel):
    email: EmailStr
    password: str


class SUserGet(BaseModel):
    id: int
    email: str
