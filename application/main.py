from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from application.controllers.authentication import authentication
from .db import get_db

app = FastAPI(docs_url="/doc")

app.include_router(authentication)


@app.get("/")
def main(db: Session = Depends(get_db)):
    """
    This is the main function.
    """
    q = db
    return {"message": "Hello World"}
