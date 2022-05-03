from fastapi import FastAPI

app = FastAPI()

@app.get("/")

async def get_hello():
    return {"greetings": "Hello World!"} 

@app.get("/items/{item_id}")

async def get_item(item_id: int, count:int = 1, msg:str = "Bye!"):
    return {"fetch": f"Fetched {count} of {item_id}... {msg}"}
    
