import json
from typing import List

from fastapi import FastAPI, HTTPException

from src.db.connection import db_connection
from src.models.puppy import PuppyGetter, PuppySetter
from src.modules.puppy import Puppy

app = FastAPI()

puppy_module = Puppy(db_connection)

@app.get("/")
def hello():
    puppies = puppy_module.get_all()
    print(puppies)
    return json.dumps(puppies)


@app.post("/puppy")
async def create_puppy(puppy: PuppySetter):
    puppy_module.insert(puppy.dict())
    return True


@app.get("/puppy")
def get_puppies():
    puppies = puppy_module.get_all()
    res = []
    for puppy_values in puppies:
        res.append({"id": puppy_values[0], "name": puppy_values[1], "breed": puppy_values[2]})

    return res


@app.get("/puppy/{id}")
def get_puppy(id: int):
    puppy = puppy_module.get_by_id(id)
    return json.dumps(puppy[0])


@app.put("/puppy/{id}")
def get_puppy(id: int, puppy: PuppySetter):
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
