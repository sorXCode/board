from datetime import datetime
from sqlalchemy import (
    Column,
    Integer,
    Text,
    DateTime
)


from .meta import Base


class Feedback(Base):
    __tablename__ = "feedbacks"
    id = Column(Integer, primary_key=True)
    subject = Column(Text, nullable=False)
    full_name = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    message = Column(Text, nullable=False)
    # time = Column(DateTime, default=datetime.now)
