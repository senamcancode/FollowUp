from typing import Optional
import os
from dotenv import load_dotenv
import logging


import psycopg2
from psycopg2.extensions import connection as PGConnection, cursor as PGCursor

class DatabaseConnection:
    """
    Singleton class for managing database connections.
    """

    _instance: Optional ["DatabaseConnection"] = None
    _connection: Optional[PGConnection] = None
    _cursor: Optional[PGCursor]

    db_name = os.getenv("NAME")
    db_user = os.getenv("USER")
    db_password = os.getenv("PASSWORD")
    db_port = os.getenv("PORT")
    db_host = os.getenv("HOST")
    
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    def __new__(cls):
        
        load_dotenv()

        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._connection = psycopg2.connect(
                database=cls.db_name,
                user=cls.db_user,
                password=cls.db_password,
                port=cls.db_port,
                host=cls.db_host
            )
            
            cls.logger.info(f"...Connecting to database {cls.db_name}")

            cls._instance._cursor = cls._instance._connection.cursor()
        return cls._instance
    # The above can be changed to a connection pool when you have multiple users
    

    def __init__(self):
        if not getattr(self, '_initialized', False):
            self.connection = self._instance._connection
            self.cursor = self._instance._cursor
            self._initialized = True


    def query(self, query: str, params: Optional[tuple] = None) -> Optional[list]:

        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
        
            if query.strip().lower().startswith("select"):
                db_rows = self.cursor.fetchall()
                return db_rows
            else:
                self.connection.commit()
                return []
        except Exception as e:
            self.connection.rollback()
            raise e            

    def disconnect(self):
        """
        Close the connection to the database. 
        """
        self.logger.info("Closing the database connection")


        self.connection.close()
        self.cursor.close()

        self.logger.info("Successful closure of database connection")


# https://softwareengineering.stackexchange.com/questions/200522/how-to-deal-with-database-connections-in-a-python-library-module       # 