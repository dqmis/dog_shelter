import json
from typing import List

from fastapi import FastAPI, HTTPException

from src.db.connection import db_connection
from src.models.puppy import Puppy as PuppyModel
from src.modules.puppy import Puppy

app = FastAPI()

puppy_module = Puppy(db_connection)

@app.get("/")
def hello():
    puppies = puppy_module.get_all()
    print(puppies)
    return json.dumps(puppies)


@app.post("/puppy")
async def create_puppy(puppy: PuppyModel):
    puppy_module.insert(puppy.dict())
    return True


@app.get("/puppy")
def get_puppies():
    puppies = puppy_module.get_all()
    return json.dumps(puppies)


@app.get("/puppy/{id}")
def get_puppy(id: int):
    puppy = puppy_module.get_by_id(id)
    return json.dumps(puppy[0])


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
