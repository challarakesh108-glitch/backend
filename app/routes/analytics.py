from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Account, EmailLog

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/stats")
def stats(db: Session = Depends(get_db)):
    total_accounts = db.query(Account).count()
    total_logs = db.query(EmailLog).count()
    total_replies = db.query(EmailLog).filter(EmailLog.status == "replied").count()

    return {
        "accounts": total_accounts,
        "emails": total_logs,
        "replies": total_replies
    }


@router.get("/reputation")
def reputation(db: Session = Depends(get_db)):
    accounts = db.query(Account).all()

    return [
        {
            "email": a.email,
            "reputation": a.reputation_score
        }
        for a in accounts
    ]