from ctypes import Union

from pydantic import BaseModel
import datetime


class User(BaseModel):
    username: str
    email: str
    full_name: str
    is_active: bool

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    is_active: bool
    password: str
    birthday: datetime.date
    phone_number: str
