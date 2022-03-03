"""
This is db Types
"""
from enum import Enum

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseTypes(Enum):
    sqlite = 1
    postgres = 2


class DatabaseBase:
    """
    This is DatabaseBase
    """

    def __init__(self):
        self._db: DatabaseTypes = DatabaseTypes.sqlite

    def __repr__(self):
        return f"<DatabaseBase: {self.db}>"

    def session_local(self) -> sessionmaker:
        """
        This is session_local generator
        """
        raise NotImplementedError


class Postgresql(DatabaseBase):
    """
    This is Postgresql
    """

    def __init__(self, username: str, password: str, host: str, port: str, db: str, auto_commit: bool = False):
        super().__init__()
        self._db = DatabaseTypes.postgres
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        self.db = db
        self.auto_commit = auto_commit

    def session_local(self) -> sessionmaker:
        """
        This is session_local generator
        """
        sql_conn = f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.db}"

        engine = create_engine(
            sql_conn
        )
        return sessionmaker(autocommit=self.auto_commit, autoflush=False, bind=engine)


class Sqlite3(DatabaseBase):
    """
    This is Sqlite3
    """

    def __init__(self, db_file: str):
        super().__init__()
        self._db = DatabaseTypes.sqlite
        self.db_file = db_file

    def session_local(self) -> sessionmaker:
        """
        This is session_local generator
        """
        sql_conn = f"sqlite:///{self.db_file}"

        engine = create_engine(
            sql_conn, connect_args={"check_same_thread": False}
        )
        return sessionmaker(autocommit=False, autoflush=False, bind=engine)
