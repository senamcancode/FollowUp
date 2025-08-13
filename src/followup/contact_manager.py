from followup.db_connection import DatabaseConnection


class ContactManager: 
    """
    Class for managing contacts 

    Creates a new contact 
    Gets contact data 
    Updates contact data 
    Deletes contact data 
    """

    # create a new contact 
    db = DatabaseConnection.create()

    