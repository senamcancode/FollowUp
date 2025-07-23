import unittest
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError


from db_connection import DatabaseConnection

class TestDatabaseConnectio(unittest.TestCase):

    def setUp(self):
        self.db_connection = DatabaseConnection()

    def test_get_session_returns_session(self):
        """
          Test if get_session returns a valid Session object.
        """
        
        session = self.db_connection.get_session()
        self.assertIsInstance(session, Session)
        session.close()

    def test_database_name_is_correct(self):
        """
        Test to get the database name of the database connected
        """    

        db_name = self.db_connection.engine.url.database
        self.assertEqual(db_name, "follow_up_db")