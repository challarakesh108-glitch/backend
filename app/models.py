from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from app.database import Base


class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    is_active = Column(Boolean, default=True)

    daily_limit = Column(Integer, default=5)
    sent_today = Column(Integer, default=0)
    received_today = Column(Integer, default=0)

    reputation_score = Column(Float, default=10.0)
    positive_reply_ratio = Column(Float, default=0.0)


class EmailLog(Base):
    __tablename__ = "email_logs"

    id = Column(Integer, primary_key=True, index=True)

    sender_email = Column(String)
    receiver_email = Column(String)

    subject = Column(String)
    message = Column(String)

    status = Column(String, default="sent")