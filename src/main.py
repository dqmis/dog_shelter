from typing import List

from fastapi import FastAPI, HTTPException

from src.db.connection import db_connection
from src.models.puppy import Puppy
from src.serializers.puppy import PuppyGetter, PuppySetter

app = FastAPI()

puppy_module = Puppy(db_connection)

@app.get("/")
def hello():
    return {"message": "Hello, world!"}


@app.get("/puppy", response_model=List[PuppyGetter])
def get_puppies():
    puppies = puppy_module.get_all()
    return puppies


@app.get("/puppy/{id}", response_model=PuppyGetter)
def get_puppy(id: int):
    puppy = puppy_module.get_by_id(id)
    return puppy


@app.post("/puppy", response_model=PuppyGetter)
async def create_puppy(puppy: PuppySetter):
    puppy = puppy_module.insert(puppy.dict())
    return puppy


@app.delete("/puppy/{id}", status_code=200)
async def delete_puppy(id: int):
    puppy_deleted = puppy_module.delete_by_id(id)
    if not puppy_deleted:
        raise HTTPException(status_code=204, detail="Record not found!")


@app.put("/puppy/{id}", status_code=200)
async def update_puppy(id: int, puppy: PuppySetter):
    updated_puppy = puppy_module.update(puppy.dict(), id)
    if not updated_puppy:
        raise HTTPException(status_code=204, detail="Record not found!")
    return updated_puppy
