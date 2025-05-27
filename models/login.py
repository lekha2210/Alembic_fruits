from sqlalchemy import Column, Integer, String
from core.db import Base

class Login(Base):
    __tablename__ = "logins"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String, unique=True, index=True)

    def __repr__(self):
        return f"Login(id={self.id}, username={self.username})"