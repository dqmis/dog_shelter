import uuid
from typing import Dict, Optional


class Puppy:
    def __init__(self, breed: str, name: str, age: int) -> None:
        self._breed = breed
        self._name = name
        self._age = age
        self._secret_id = uuid.uuid4().hex

    def serialize(self) -> Dict:
        return {"breed": self._breed, "name": self._name, "age": self._age}

    def update(self, name: str, age: int, breed: Optional[str] = None) -> bool:
        if name:
            self._name = name
        if age:
            self._age = age
        return True
