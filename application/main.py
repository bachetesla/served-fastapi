from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from .db import get_db

app = FastAPI()


@app.get("/")
def main(db: Session = Depends(get_db)):
    """
    This is the main function.
    """
    q = db
    return {"message": "Hello World"}
