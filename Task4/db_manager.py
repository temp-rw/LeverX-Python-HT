import mysql.connector
from typing import Any, List, Dict, Tuple, Union


class IDBManager:
    def create(self, table: str, column_value: List[Dict]):
        raise NotImplementedError

    def read(self, table: str, columns: List[str], limit: int = None):
        raise NotImplementedError

    def update(self, table: str, column_value: Dict, limit: int = None):
        raise NotImplementedError

    def delete(self, table: str, column_value: Dict, limit: int = None):
        raise NotImplementedError

    def _run_query(self, query: str, value: Union[Tuple, List[Tuple]]):
        raise NotImplementedError


class DBManager(IDBManager):
    def __init__(self, host: str, user: str, password: str, database: str):
        self.db = {"host": host, "user": user, "password": password, "database": database}

    def create(self, table: str, columns_values: List[Dict]):
        if table.isalnum():
            keys = "(" + ", ".join([key for key in columns_values[0].keys()]) + ")"
            value_positions = "(" + ", ".join(["%s" for _ in columns_values[0].keys()]) + ")"
            values = []
            for item in columns_values:
                query_template = rf"INSERT INTO {table} {keys} VALUES {value_positions}"

                temp_values = []
                for key in item.keys():
                    temp_values.append(item[key])
                values.append(tuple(temp_values))

            self._run_query(query_template, values)

    def read(self, table: str, columns: List[str], limit: int = None):
        pass

    def update(self, table: str, column_value: Dict, limit: int = None):
        pass

    def delete(self, table: str, column_value: Dict, limit: int = None):
        pass

    def _run_query(self, query: str, value: Union[Tuple, List[Tuple]]):
        if isinstance(value, List):
            with mysql.connector.connect(**self.db) as connection:
                cursor = connection.cursor()
                cursor.executemany(query, value)
                connection.commit()
        elif isinstance(value, Tuple):
            with mysql.connector.connect(**self.db) as connection:
                cursor = connection.cursor()
                cursor.execute(query, value)
                connection.commit()
