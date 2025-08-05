from followup.db_connection import DatabaseConnection


class ContactManager: 
    """
    Class for managing contacts 
    """

    # create a new contact 
    db = DatabaseConnection.create()