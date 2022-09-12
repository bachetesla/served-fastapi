"""
This is users Model file and helpers.
"""
from datetime import datetime

from application.db import Base
from sqlalchemy import Column, String, Integer, DateTime, Boolean


class User(Base):
    """
    This is user Model.
    """
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)

    first_name = Column(String)
    last_name = Column(String)

    birthday = Column(DateTime)

    username = Column(String)
    email = Column(String)

    password = Column(String)

    phone_number = Column(String)

    created_at = Column(DateTime)
    is_active = Column(Boolean)

    @property
    def full_name(self) -> str:
        """
        This is going to return the full name!
        :return: fullname
        """
        return str(self.first_name + " " + self.last_name)

    @property
    def age(self):
        """
        This is going to return the user age!
        :return: age
        """
        return (datetime.utcnow() - self.birthday).days / 365
