import psycopg2

class DatabaseConnection:
    """
    Singleton class for managing database connections.
    """

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._connection = None #TO DO - initialize database connection here 
        return cls._instance
    

    def __init__(self):
        self.connection = self._instance.connection
        self.cursor = self._instance.cursor


    def query(self, query, params=None):


    def disconnect(self):
        """
        Close the connection to the database. 
        """
        self.connection.close()
        self.cursor.close()



# https://softwareengineering.stackexchange.com/questions/200522/how-to-deal-with-database-connections-in-a-python-library-module       # 