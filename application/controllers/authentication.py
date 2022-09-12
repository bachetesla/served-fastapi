from datetime import datetime, timedelta
from typing import Union

from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt

from application.config import SECRET_KEY, ALGORITHM
from application.crud import UserCRUD
from application.db import get_db
from application.schemas.authentication import TokenData, Token
from application.schemas.users import User, UserCreate
from sqlalchemy.orm import Session
from application.config import pwd_context

ACCESS_TOKEN_EXPIRE_MINUTES = 30

authentication = APIRouter(
    prefix="/authentication",
    tags=['authentication'],
    responses={404: {"MSG": "not-found"}},
    dependencies=[Depends(get_db)]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/authentication/token")


def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = UserCRUD(db).read("username", token_data.username)
    if user is None:
        raise credentials_exception
    return user


def get_current_active_user(current_user: User = Depends(get_current_user)):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@authentication.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = UserCRUD(db).authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = UserCRUD(db).create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@authentication.get("/users/me/", response_model=User)
def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@authentication.post("/signup", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserCRUD(db).create(user)
