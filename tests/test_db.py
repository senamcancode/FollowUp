import unittest
from sqlalchemy.orm import Session
from followup.db_connection import DatabaseConnection

class TestDatabaseConnection(unittest.TestCase):

    def setUp(self):
        self.db = DatabaseConnection.create()

    def test_database_name(self):
        db_name = self.db.engine.url.database
        expected_name = "follow_up_db" 
        self.assertEqual(db_name, expected_name)    

    def test_engine_connection(self):
        '''
        Test if engine connects without errors
        '''
        try:
            with self.db.engine.connect() as conn:
                self.assertTrue(conn.closed == False)
        except Exception as e:
            self.fail(f"Engine connection failed: {e}")

    def test_get_session(self):
        '''
        Test if get_session returns a valid Session
        '''
        session = None
        try:
            session = self.db.get_session()
            self.assertIsInstance(session, Session)
        except Exception as e:
            self.fail(f"Failed to get session: {e}")
        finally:
            if session:
                session.close()

if __name__ == "__main__":
    unittest.main()