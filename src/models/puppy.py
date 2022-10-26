from typing import Optional

from pydantic import BaseModel


class Puppy(BaseModel):
    name: str
    breed: str
