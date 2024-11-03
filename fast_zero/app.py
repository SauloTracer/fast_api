from fastapi import FastAPI
from fast_zero.schemas import Message
from http import HTTPStatus

app = FastAPI()


@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    """API entry point"""
    return {"message": "Hello -=FastApi"}
