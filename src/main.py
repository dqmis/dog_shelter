from typing import List

from fastapi import FastAPI, HTTPException

from src.db.connection import db_connection
from src.models.puppy import Puppy as PuppyModel
from src.modules.puppy import Puppy

app = FastAPI()

puppy_module = Puppy(db_connection)

puppies: List[Puppy] = []


@app.get("/")
def hello():
    return {"message": "Hello, World!"}


@app.post("/puppy")
async def create_puppy(puppy: PuppyModel):
    puppies.append(Puppy(**puppy.dict()))
    return [p.serialize() for p in puppies]


@app.get("/puppy")
def get_puppies():
    return [p.serialize() for p in puppies]


@app.get("/puppy/{id}")
def get_puppy(id: int):
    try:
        return puppies[id].serialize()
    except IndexError:
        raise HTTPException(status_code=404, detail="Puppy not found :(")


@app.put("/puppy/{id}")
def get_puppy(id: int, puppy: PuppyModel):
    if id >= len(puppies):
        raise HTTPException(status_code=404, detail="Puppy not found :(")
    our_puppy = puppies[id]
    our_puppy.update(**puppy.dict())
    return our_puppy.serialize()


@app.delete("/puppy/{id}")
def get_puppy(id: int):
    try:
        puppies.pop(id)
        return [p.serialize() for p in puppies]
    except IndexError:
        raise HTTPException(status_code=404, detail="Puppy not found :(")
