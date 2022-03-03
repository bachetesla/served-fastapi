"""
This is db connection module.
"""

from sqlalchemy.ext.declarative import declarative_base

from .config import DATABASE

Base = declarative_base()


# Dependency
def get_db():
    """
    This is a function to get db connection.
    :return: db connection
    """
    db = DATABASE
    try:
        yield db
    finally:
        db.close()
