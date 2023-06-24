import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Protocol


class Store(Protocol):
    path: str = ""

    def establish_store(self, db_name: str) -> None:
        """
        Establish a connection to the store
        For files, check if the path/file exists, if not create it

        For sql, check if the path/db exists, if not create it
        create a connection
        return a cursor
        """
        ...

    def store_record(self, record: Any) -> None:
        ...


@dataclass()
class FileStore:
    path: str = "data/test.txt"

    def establish_store(self, db_name: str) -> None:
        """
        Establish a connection to the store
        For files, check if the path/file exists, if not create it

        For sql, check if the path/db exists, if not create it
        create a connection
        return a cursor
        """
        Path(self.path).touch()

    def store_record(self, record: Any) -> None:
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(record)
            f.write("\n")


@dataclass()
class SQLiteStore:
    """SQLite store"""

    path: str = "data/reddit.db"
    created: bool = False

    def establish_store(self) -> None:
        self.client = sqlite3.connect(self.path, timeout=10)
        self.cur = self.client.cursor()

    def generate_table_create_statement(self, table_name: str, schema: Any) -> str:
        fields = ",".join([f"{i[0]} {i[1]}" for i in list(schema)])
        return f"create table if not exists {table_name} ({fields});"

    def generate_insert_statement(self, table_name: str, dat: Any, schema: Any) -> str:
        # # insert section
        keys = ""
        vals = ""
        for k, v in dat:
            if k != "schema":
                if v is None and schema[k] != "text":
                    v = 0
                keys += f"{k},"
                vals += f"'{clean_val(str(v))}'," if schema[k] == "text" else f"{v},"
        return f"INSERT INTO {table_name} ({keys.rstrip(',')}) VALUES ({vals.rstrip(',')});"

    def store_record(self, dat: Any) -> None:
        """
        Accept a generic object and create a sql insert statement out of it.
        Is this where I should convert over to the sql statement or should i do it in the object?
        A dict comes in, a sql statement comes out
        """
        # there must be a schema dict object called schema as part of record.
        # # create table if not exists comments (author text, type text, body text, down int, likes int, subreddit_name_prefixed text, subreddit_id text, contraversiality float, ups int, author_flair_type text)
        table_name = dat.__class__.__name__.lower()
        schema = dat.schema
        if not self.created:
            create_statement = self.generate_table_create_statement(
                table_name, schema.items()
            )
            self.cur.execute(create_statement)
            self.client.commit()
            self.created = True

        sql_insert = self.generate_insert_statement(
            table_name, dat.__dict__.items(), schema
        )
        print(sql_insert)
        self.cur.execute(sql_insert)
        self.client.commit()

    def __post_init__(self):
        self.establish_store()


def clean_val(val: str) -> str:
    return val.replace("'", "").replace("\n", "").replace(",", "")


## I would like one more specific level to call out sqlish
# class SQLish(Protocol):
#     """SQLish protocol"""
#     def read(self, table_name: str, record: Any) -> None:
#         ...

#     def insert(self, table_name: str, record: Any) -> None:
#         ...

# def delete(self, table_name: str, record: Any) -> None:
#     ...

# def update(self, table_name: str, record: Any) -> None:
#     ...
