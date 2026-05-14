from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Account
from app.schemas import AccountCreate, AccountResponse

router = APIRouter(prefix="/accounts", tags=["Accounts"])


# Create Account
@router.post("/", response_model=AccountResponse)
def create_account(account: AccountCreate, db: Session = Depends(get_db)):

    existing = db.query(Account).filter(Account.email == account.email).first()

    if existing:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_account = Account(
        email=account.email,
        is_active=True,
        daily_limit=5
    )

    db.add(new_account)
    db.commit()
    db.refresh(new_account)

    return new_account


# Get All Accounts
@router.get("/", response_model=list[AccountResponse])
def get_accounts(db: Session = Depends(get_db)):
    return db.query(Account).all()


# Get One Account
@router.get("/{account_id}", response_model=AccountResponse)
def get_account(account_id: int, db: Session = Depends(get_db)):

    account = db.query(Account).filter(Account.id == account_id).first()

    if not account:
        raise HTTPException(status_code=404, detail="Account not found")

    return account


# Enable / Disable
@router.put("/{account_id}/toggle")
def toggle_account(account_id: int, db: Session = Depends(get_db)):

    account = db.query(Account).filter(Account.id == account_id).first()

    if not account:
        raise HTTPException(status_code=404, detail="Account not found")

    account.is_active = not account.is_active

    db.commit()

    return {
        "message": "Updated successfully",
        "is_active": account.is_active
    }