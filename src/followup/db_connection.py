from typing import Optional
import os
from dotenv import load_dotenv
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session



class DatabaseConnection:
    """
    Class for for managing database connections.
    """
    def __init__(self):
        load_dotenv()

        db_name = os.getenv("NAME")
        db_user = os.getenv("USER")
        db_password = os.getenv("PASSWORD")
        db_port = os.getenv("PORT")
        db_host = os.getenv("HOST")    

        if not all([db_name, db_user, db_password, db_port, db_host]):
            raise ValueError("Missing one or more required databse environment variables")
        
        self.database_url = f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"

        self.engine = create_engine(self.database_url, pool_pre_ping=True)
        self.session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)


    def get_session(self) -> Session: 
        return self.session()


    

# https://softwareengineering.stackexchange.com/questions/200522/how-to-deal-with-database-connections-in-a-python-library-module       #