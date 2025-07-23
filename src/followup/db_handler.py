from typing import Optional
import os
from dotenv import load_dotenv
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseConnection:
    """
    Script for managing database connections.
    """
    db_name = os.getenv("NAME")
    db_user = os.getenv("USER")
    db_password = os.getenv("PASSWORD")
    db_port = os.getenv("PORT")
    db_host = os.getenv("HOST")
    
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    load_dotenv()

    if not all([db_name, db_user, db_password, db_port, db_host]):
        raise EnvironmentError("One or more database variables are misisng")

    DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"

    engine = create_engine(DATABASE_URL, pool_pre_ping=True)

    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# https://softwareengineering.stackexchange.com/questions/200522/how-to-deal-with-database-connections-in-a-python-library-module       #