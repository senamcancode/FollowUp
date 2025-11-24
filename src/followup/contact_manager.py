from followup.db_connection import DatabaseConnection
from models import Contact, engine
import logging

class ContactManager:
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
            new_contact= Contact(**new_contact_dict_data)
            self.db_session.add(new_contact)
            self.db_session.commit()
            self.logger.info("Successfully created new contact")
            return  new_contact

        except Exception as e:
            try:
                self.db_session.rollback()
            except Exception:
                pass
                self.logger.error(f"Failed to create new contact, rolling back database changes. Error {e}")
            return None
        
        finally:
            DatabaseConnection.close()      


    def get_contact(self, saved_contact_data: dict) -> bool:
        self.logger.info("Retrieving contact")

        try:
            saved_contact = self.db_session.query(Contact).filter_by(**saved_contact_data).first()
            return saved_contact
        except Exception as e:
            try: 
                self.db_session.rollback()
            except Exception:     
                self.logger.error(f"Failed to delete {saved_contact}, rolling back database changes. Error {e}")
            return None




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
            contact = self.db_session.get(Contact, contact_uuid)

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
        

    
    def close(self) -> None:
        """Close the session associated with this manager"""
        try:
            self.db_session.close()
        except Exception:
            pass   

#- get_contact_info_by_id(id)
#- get_last_meeting_date_for_contact(contact_id)
#- get_last_meeting_date_for_all_contacts()
#- get_last_meeting_talking_points(contact_id)
#- get_contact_email_address(contact_id)
#- get_contact_message_address(contact_id)
#- get_contact_quirks(contact_id)
#- get_contact_profession(contact_id)
#- get_meeting_frequency(contact_id)
#- get_all_contacts         