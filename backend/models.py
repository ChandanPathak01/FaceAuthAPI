from sqlalchemy import Column, String, Integer, DateTime, Text, func
from sqlalchemy.dialects.postgresql import UUID
import uuid
from .database import Base
class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    aadhaar = Column(String, nullable=False, index=True)
    face_encoding = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())