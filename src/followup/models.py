import uuid

from sqlalchemy import Column, String, Interval, UUID, Text, CheckConstraint, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Contact(Base):
    __tablename__ = "contacts"

    contact_id = Column(UUID, primary_key=True, default=uuid.uuid4, name="ContactID")
    first_name = Column(String(255), nullable=False, name="FirstName")
    last_name = Column(String(255), nullable=True, name="LastName")
    profession = Column(String(255), name="Profession")
    contact_quirks = Column(String(255), name="ContactQuirks")
    contact_email = Column(String(255), name="ContactEmail")
    contact_message_info= Column(String(255), name="ContactMessageInfo")
    last_meeting_date = Column(Date, name="DateOfLastMeeting")
    last_meeting_talking_points = Column(Text, name="TalkingPointsOfLastMeeting")
    meeting_frequency= Column(Interval, name="MeetingFrequency")

    __table_args__ = (
        CheckConstraint(
            '("Contact email" IS NOT NULL OR "ContactMessageInfo" IS NOT NULL ',
            name='contact_email_or_message_required'
        )
    )

    def __repr__(self):
        return(
            f"<Contact(first_name={self.first_name}, "
            f"last_name={self.last_name}, "
            f"profession={self.profession}, "
            f"contact_quirks={self.contact_quirks}, "
            f"contact_email={self.contact_email}, "
            f"contact_message_info={self.contact_message_info}, "
            f"last_meeting_date={self.last_meeting_date}, "
            f"last_meeting_talking_points={self.last_meeting_talking_points}, "
            f"meeting_frequency={self.meeting_frequency})>"
        )