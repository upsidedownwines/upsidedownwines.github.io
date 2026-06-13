from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import json
import os

app = FastAPI()

class Destination(BaseModel):
    id: str
    name: str
    description: str
    image_url: str

@app.get("/api/destinations", response_model=List[Destination])
async def get_destinations():
    json_path = os.path.join(os.path.dirname(__file__), "..", "src", "data", "destinations.json")
    with open(json_path, "r") as f:
        return json.load(f)

@app.get("/api/hello")
async def hello():
    return {"message": "Hello from FastAPI backend!"}
