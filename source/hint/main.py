from fastapi import FastAPI

# Import Union since our Item object will have tags that can be strings or a list.
from typing import Union

# BaseModel from Pydantic is used to define data objects.
# These data objects HAVE to be of the specified type or an error is generated.
from pydantic import BaseModel

# Declare the data object with its components and their type.
class TaggedItem(BaseModel):
    name: str
    tags: Union[str, list]
    item_id: int

app = FastAPI()

# This allows us to send the data (our TaggedItem) via POST to the API.
@app.post("/items/")
async def create_item(item: TaggedItem):
    return item
    
