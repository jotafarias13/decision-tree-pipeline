
from fastapi import FastAPI

# Instantiate an object that will be used as an app by uvicorn
app = FastAPI()

# Define a get request on a specified endpoint
@app.get("/")
async def say_hello():
    return {"greeting": "Hello World!"}
