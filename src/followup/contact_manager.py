from models import Contact
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

import uuid

class ContactManager:
    def __init__(self, session: Session):
        self.session = session

    def create_contact(self, first_name: str, last_name: str, **kwargs) -> Contact:
        new_contact = Contact(
            first_name=first_name,
            last_name=last_name,
            **kwargs  # Other optional fields
        )
        self.session.add(new_contact)
        self.session.commit()
        self.session.refresh(new_contact)
        return new_contact

    def get_contact_by_id(self, contact_id: uuid.UUID) -> Contact:
        return self.session.query(Contact).filter(Contact.contact_id == contact_id).first()