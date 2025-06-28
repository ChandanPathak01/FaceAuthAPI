from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
from datetime import datetime

class RegisterRequest(BaseModel):
    name:str
    phone:str
    email:EmailStr
    aadhar: str

class MatchRequest(BaseModel):
    aadhaar: str

class USerOut(BaseModel):
    id: UUID
    name: str
    phone: str
    email: EmailStr
    aadhaar: str
    created_at: datetime

    class Config:
        from_attributes = True

class MatchResult(BaseModel):
    user: USerOut
    match_percent: float