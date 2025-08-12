from src.followup.db_connection import DatabaseConnection
import pytest
import os
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.engine import Engine 
import logging 

# Test that the singleton pattern works (only one instance is created).
# Test that the database engine is created successfully with valid environment variables.
# Test that a session can be created from the connection.
# Test that closing the engine logs the correct message.
# Test that missing required environment variables raises an appropriate error.

@pytest.fixture()
def set_up_test_db(monkeypatch):
    monkeypatch.setenv("USER", "test_user")
    monkeypatch.setenv("PASSWORD", "test_pwd")
    monkeypatch.setenv("NAME", "test_name")
    monkeypatch.setenv("HOST", "localhost")
    monkeypatch.setenv("PORT", "5432") 


def test_db_singleton(set_up_test_db) -> None:
    """
    A unit test to check that the database instance is a singleton.
    """
    db_instance = DatabaseConnection.create()
    second_db_instance = DatabaseConnection.create()
    
    assert db_instance is not None
    assert db_instance == second_db_instance

def test_create_engine(set_up_test_db) -> None:
    """
    Test that the database engine is created successfully.
    """
    db_instance = DatabaseConnection.create()
    engine = db_instance.engine
    
    assert engine is not None 
    assert isinstance(engine, Engine)

def test_session_created_from_db_connection(set_up_test_db) -> None:
    """
    Test that a session can be created from the connection.
    """
    db_instance = DatabaseConnection.create()
    db_session = db_instance.get_session()

    assert db_session is not None 
    assert isinstance(db_session, Session)


def test_close_function_generates_logs_message(set_up_test_db, caplog) -> None:
    """
    Test that the close() method generates a log message.
    """
    with caplog.at_level(logging.INFO):
        db_instance = DatabaseConnection.create()
        db_instance.close()
    assert("Database engine disposed" in caplog.text)    

def test_missing_environmental_variables_raise_error(monkeypatch) -> None:
    """
    Test that missing required environment variables raises an appropriate error.
    """
    DatabaseConnection._DatabaseConnection__instance = None

    monkeypatch.delenv("USER", raising=False)
    monkeypatch.delenv("PASSWORD", raising=False)
    monkeypatch.delenv("NAME", raising=False)
    monkeypatch.delenv("HOST", raising=False)
    monkeypatch.delenv("PORT", raising=False) 

    with pytest.raises(Exception) as e:
        db_instance = DatabaseConnection.create()
        db_engine = db_instance.create_engine()



