from typing import Optional
import os
from dotenv import load_dotenv
import logging
import sqlalchemy
from sqlalchemy.orm import sessionmaker, Session


class DatabaseConnection:
    """
    Class for for managing database connections.
    """
    __instance = None
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)


    def __init__(self):

        if DatabaseConnection.__instance is not None: 
            raise Exception(
                "This class is a singleton, use DatabaseConnection.create()")
        else:
            DatabaseConnection.__instance = self 
        self.engine = self.create_engine()
        self.SessionLocal = sessionmaker(bind=self.engine, autoflush=False, autocommit=False)

    @classmethod
    def create(cls):
        if cls.__instance is None:
            cls.__instance = cls()
            cls.logger.info(f"Created database connection for database {os.getenv('NAME')}")
        return cls.__instance        
    
    def create_engine(self):
        """Fetch credentials from environment variables and create database connection"""
        load_dotenv() 

        db_engine = "postgresql"
        db_name = os.getenv("NAME")
        db_user = os.getenv("USER")
        db_password = os.getenv("PASSWORD")
        db_port = os.getenv("PORT")
        db_host = os.getenv("HOST")   
        
        if not all([db_name, db_user, db_password, db_port, db_host]):
            missing = [var for var in ["NAME", "USER", "PASSWORD", "PORT", "HOST"] if os.getenv(var) is None]
            raise ValueError(f"Missing required environment variables: {','.join(missing)}")
        
        return sqlalchemy.create_engine(f'{db_engine}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
    
    def get_session(self) -> Session:
        try:
            return self.SessionLocal()
        except Exception as e:
            self.logger.error("Failed to create session: %s", e)
            raise
    
    def close(self):
        self.engine.dispose()
        self.logger.info("Database engine disposed")    


    

# https://softwareengineering.stackexchange.com/questions/200522/how-to-deal-with-database-connections-in-a-python-library-module       #