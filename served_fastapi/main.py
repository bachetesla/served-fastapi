from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def main():
    """
    This is the main function.
    """
    return {"message": "Hello World"}
