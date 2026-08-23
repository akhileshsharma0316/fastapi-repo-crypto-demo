from datetime import datetime, timezone

from sqlalchemy import Column, Integer, String, Boolean, DateTime

from core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True,nullable=False)
    email = Column(String, unique=True, index=True,nullable=False)
    hashed_email = Column(String,nullable=False)
    password = Column(String,nullable=False)
    fullname = Column(String,nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))