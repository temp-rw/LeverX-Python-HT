from typing import List, Dict, Tuple, Union

import mysql.connector


class IDBManager:
    def create(self, table: str, column_value: List[Dict]):
        raise NotImplementedError

    def read(self, table: str, columns: List[str]):
        raise NotImplementedError

    def _run_sql_query(self, query: str, method: str, value: Union[Tuple, List[Tuple]] = None):
        raise NotImplementedError


class DBManager(IDBManager):
    def __init__(self, **kwargs):
        self.option_file = kwargs

    def create(self, table: str, columns_values: List[Dict]):
        if table.isalnum():
            columns = "(" + ", ".join([key for key in columns_values[0].keys()]) + ")"
            value_positions = "(" + ", ".join(["%s" for _ in columns_values[0].keys()]) + ")"
            values = []
            query_template = None
            for item in columns_values:
                query_template = rf"INSERT INTO {table} {columns} VALUES {value_positions}"

                temp_values = []
                for key in item.keys():
                    temp_values.append(item[key])
                values.append(tuple(temp_values))

            self._run_sql_query(query_template, "insert", values)

    def read(self, table: str, columns: List[str]) -> Union[None, List[Dict]]:
        result = []
        if table.isalnum():
            columns_string = ", ".join(columns)
            query_template = rf"SELECT {columns_string} FROM {table}"
            response = self._run_sql_query(query_template, "select")

            for row in response:
                element = dict()
                for index, column in enumerate(columns):
                    element[column] = row[index]
                result.append(element)

        return result

    def get_data_by_custom_query(self, columns: List[str], request_query: str) -> List[Dict]:
        response = self._run_sql_query(request_query, method="select")
        return self.response_to_dict(columns, response)

    @staticmethod
    def response_to_dict(columns: List[str], response: List[Tuple]) -> List[Dict]:
        result = []
        for row in response:
            element = dict()
            for index, column in enumerate(columns):
                element[column] = row[index]
            result.append(element)
        return result

    def _run_sql_query(
        self, query: str, method: str, value: Union[Tuple, List[Tuple]] = None
    ) -> Union[None, List[Tuple]]:
        with mysql.connector.connect(**self.option_file) as connection:
            cursor = connection.cursor()

            if method == "insert":
                if value is not None:
                    if isinstance(value, List):
                        cursor.executemany(query, value)
                        connection.commit()
                    elif isinstance(value, Tuple):
                        cursor.execute(query, value)
                        connection.commit()
            else:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
