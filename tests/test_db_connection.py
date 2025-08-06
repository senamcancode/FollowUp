from src.followup.db_connection import DatabaseConnection
import pytest
import os
from dotenv import load_dotenv


# Test that the singleton pattern works (only one instance is created).
# Test that the database engine is created successfully with valid environment variables.
# Test that a session can be created from the connection.
# Test that closing the engine logs the correct message.
# Test that missing required environment variables raises an appropriate error.

@pytest.fixture(autouse=True)
def set_up_test_db(monkeypatch):
    monkeypatch.setenv("USER", "test_user")
    monkeypatch.setenv("PASSWORD", "test_pwd")
    monkeypatch.setenv("NAME", "test_name")
    monkeypatch.setenv("HOST", "localhost")
    monkeypatch.setenv("PORT", "5432") 


def test_db_singleton() -> None:
    """
    A unit test to check that the database instance is a singleton.
    """
    db_instance = DatabaseConnection.create()
    second_db_instance = DatabaseConnection.create()
    
    assert db_instance is not None
    assert db_instance == second_db_instance

def test_create_engine() -> None:
    """
    Test that the database engine is created successfully.
    """
    db_instance = DatabaseConnection.create()
    engine = db_instance.engine
    
    assert engine is not None 
    from sqlalchemy.engine import Engine 
    assert isinstance(engine, Engine)

def test_session() -> None:
    """
    Test that a session can be created from the connection.
    """

    pass



