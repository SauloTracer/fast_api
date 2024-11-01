from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    """API entry point"""
    return {"message": "Hello -=FastApi"}
