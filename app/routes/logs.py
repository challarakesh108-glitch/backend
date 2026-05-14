from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import EmailLog

router = APIRouter(prefix="/logs", tags=["Logs"])


@router.get("/")
def get_logs(db: Session = Depends(get_db)):
    return db.query(EmailLog).all()