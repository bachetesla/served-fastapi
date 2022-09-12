"""
This is users CRUD
"""

from datetime import datetime, timedelta
from typing import Union

from fastapi import HTTPException
from jose import jwt
from pydantic import BaseModel

from application.config import ALGORITHM
from application.config import SECRET_KEY
from application.config import pwd_context
from application.models.users import User
from application.schemas.users import UserCreate
from .base import CRUDBase


class UserCRUD(CRUDBase):
    model = User

    def read(self, identifier, quantity) -> model:
        return self.session.query(User).filter(getattr(User, identifier) == quantity).first()

    def update(self, schema: BaseModel, identifier, quantity) -> model:
        pass

    def delete(self, identifier, quantity) -> bool:
        pass

    def create(self, schema: UserCreate) -> model:
        schema.password = pwd_context.hash(schema.password)
        user = User(**schema.dict())
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def authenticate_user(self, username: str, password: str) -> model:
        user: User = self.read("username", username)
        if not user:
            raise HTTPException(status_code=404, detail="not-found")
        if not pwd_context.verify(password, user.password):
            raise HTTPException(status_code=400, detail="password's wrong")
        return user

    def create_access_token(self, data: dict, expires_delta: Union[timedelta, None] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
