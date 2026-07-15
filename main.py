from fastapi import FastAPI
from db.dependency import get_db

# Create a FastAPI app instance
app = FastAPI()

# GET end point
@app.get("/")
def home():
    return {"message": "Hello Welcome"}
