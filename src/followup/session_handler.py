from followup.db_connection import DatabaseConnection
from models import Contact, engine
import logging

class SessionHandler:
    """
    Class for managing session

    Args:
        New contact dictionary from user input 

    Returns:
    The newly created Contact instance on success, None on failure
    """

    def __init__(self) -> None:
        self.db_session =  DatabaseConnection.get_session()
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)


    def add_new_contact(self, new_contact_dict_data: dict) -> Contact:
        self.logger.info("Creating new contact")

        try: 
            new_contact_data = Contact(**new_contact_dict_data)
            self.db_session.add(new_contact_data)
            self.db_session.commit()
            self.logger.info("Successfully created new contact")
            return  new_contact_data

        except Exception as e:
            self.db_session.rollback()
            self.logger.error(f"Failed to create new contact, rolling back database changes. Error {e}")
            return None
        
        finally:
            DatabaseConnection.close()


    def delete_contact(self, contact_uuid: str) -> bool:
        """
        Deletes a contact from the database by its UUID.

        Args:
            contact_uuid: The ID of the conatct to delete.

        Returns:
            True if the contact was successfully deleted, False otherwise.    
        """
        self.logger.info(f"...Deleting contact with contact ID: {contact_uuid}")

        try:
            contact = self.db_session.query(Contact).get(contact_uuid)

            if not contact:
                self.logger.warning(f"Contact with contact ID: {contact_uuid} not found.")
                return False

            self.db_session.delete(contact)
            self.db_session.commit()
            self.logger.info(f"Successfully deleted contact with contact ID: {contact_uuid}.")
            return True
        
        except Exception as e:
            self.db_session.rollback()
            self.logger.error(f"Failed to delete contact, with contact ID: {contact_uuid} rolling back database changes. Error {e}")
            return False
        
        finally:
            DatabaseConnection.close()

                