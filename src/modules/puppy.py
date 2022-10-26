from mysql.connector.connection_cext import CMySQLConnection

from src.modules.base import BaseModule


class Puppy(BaseModule):
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
