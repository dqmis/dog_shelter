from typing import Dict

from mysql.connector.connection_cext import CMySQLConnection

from src.models.base import BaseModel


class Puppy(BaseModel):
    __table__: str = "puppies"

    def __init__(self, db_connection: CMySQLConnection) -> None:
        super().__init__(db_connection)

    def _initialization_query(self) -> str:
        query = """CREATE TABLE IF NOT EXISTS puppies (
            id int NOT NULL AUTO_INCREMENT,
            name varchar(255) NOT NULL,
            breed varchar(255) NOT NULL,
            PRIMARY KEY(id)
        );"""
        return query
