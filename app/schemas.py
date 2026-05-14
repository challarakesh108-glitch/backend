from pydantic import BaseModel, EmailStr
from typing import Optional


class AccountCreate(BaseModel):
    email: EmailStr


class AccountResponse(BaseModel):
    id: int
    email: str
    is_active: bool
    daily_limit: int
    sent_today: int
    received_today: int
    reputation_score: float
    positive_reply_ratio: float

    class Config:
        from_attributes = True