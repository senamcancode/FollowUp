from typing import Optional
import psycopg2
from psycopg2.extensions import connection as PGConnection, cursor as PGCursor

class DatabaseConnection:
    """
    Singleton class for managing database connections.
    """

    _instance: Optional ["DatabaseConnection"] = None
    _connection: Optional[PGConnection] = None
    _cursor: Optional[PGCursor]


    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._connection = None #TO DO - initialize database connection here 
        return cls._instance

    # The above can be changed to a connection pool when you have multiple users
    

    def __init__(self):
        if not getattr(self, '_initialized', False):
            self.connection = self._instance.connection
            self.cursor = self._instance.cursor
            self._initialized = True


    def query(self, query: str, params: Optional[tuple] = None) -> Optional[list]:
        return list

    def disconnect(self):
        """
        Close the connection to the database. 
        """
        self.connection.close()
        self.cursor.close()



# https://softwareengineering.stackexchange.com/questions/200522/how-to-deal-with-database-connections-in-a-python-library-module       # 