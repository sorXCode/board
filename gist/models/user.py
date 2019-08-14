import bcrypt
from sqlalchemy import (
    Column,
    Integer,
    Text,
)

from .meta import Base


class User(Base):
    """
    The SQLAlchemy declarative model class for a User object.
    """
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(Text, nullable=False, unique=True)
    email = Column(Text, nullable=False, unique=True)
    role = Column(Text, nullable=False)
    password_hash = Column(Text)

    def set_password(self, password):
        hashdpw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.password_hash = hashdpw.decode('utf-8')

    def check_password(self, password):
        if self.password_hash is not None:
            expected_hash = self.password_hash.encode('utf-8')
            return bcrypt.checkpw(password.encode('utf-8'), expected_hash)
        return False
