from src.models.settings.base import Base
from sqlalchemy import column, String, Integer

class events(Base):
    __tablename__ = "events"

    id = column(String, primary_key=True)
    title = column(String, nullabel=False)
    details = column(String)
    slug = column(String, nullable=False)
    maximum_attendees = column(Integer)
