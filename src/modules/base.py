from abc import ABC, abstractmethod

from mysql.connector.connection_cext import CMySQLConnection


class BaseModule(ABC):
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

