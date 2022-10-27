from pydantic import BaseModel


class PuppySetter(BaseModel):
    name: str
    breed: str


class PuppyGetter(BaseModel):
    id: int
    name: str
    breed: str
