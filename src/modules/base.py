from abc import ABC, abstractmethod
from typing import Any, Dict, List, Tuple

from mysql.connector.connection_cext import CMySQLConnection


class BaseModule(ABC):
    __table__: str = None

    def __init__(self, db_connection: CMySQLConnection) -> None:
        self._db_connection = db_connection
        self._create_table()

    def _create_table(self) -> bool:
        query = self._initialization_query()
        cur = self._db_connection.cursor()
        cur.execute(query)

    @abstractmethod
    def _initialization_query(self) -> str:
        pass

    @property
    def soft_dimensions(self) -> Dict:
        return {}

    def get_all(self) -> List[Tuple]:
        cur = self._db_connection.cursor()
        cur.execute(f"SELECT * from {self.__table__}")
        return [val for val in cur]

    def get_by_id(self, id: int) -> List[Tuple]:
        cur = self._db_connection.cursor()
        cur.execute(f"SELECT * from {self.__table__} where id = {id}")
        return [val for val in cur]

    def insert(self, insert_values: Dict) -> List[Tuple]:
        cur = self._db_connection.cursor()
        insert_dimensions = ", ".join(
            [insert_title for insert_title in insert_values.keys()]
        )
        _insert_values = ", ".join(
            [f"'{insert_value}'" for insert_value in insert_values.values()]
        )
        query = f"INSERT INTO {self.__table__} ({insert_dimensions}) values ({_insert_values});"
        print(queryf"INSERT INTO {self.__table__} ({insert_dimensions}) values ({_insert_values});")
        self._db_connection.commit()
