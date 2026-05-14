import random
from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Account

scheduler = BackgroundScheduler()
engine_running = False


subjects = [
    "Hello",
    "Quick Follow Up",
    "Business Proposal",
    "Nice to Connect",
    "Checking In"
]

messages = [
    "Hope you are doing well.",
    "Let's discuss opportunities.",
    "Looking forward to hearing from you.",
    "Can we connect soon?",
    "Thanks for your response."
]


def simulate_activity():
    db = SessionLocal()

    accounts = db.query(Account).filter(Account.is_active == True).all()

    if len(accounts) < 2:
        db.close()
        return

    sender = random.choice(accounts)
    receiver = random.choice(accounts)

    while sender.id == receiver.id:
        receiver = random.choice(accounts)

    sender.sent_today += 1
    receiver.received_today += 1

    sender.reputation_score += 0.5

    db.commit()
    db.close()

    print(f"{sender.email} sent email to {receiver.email}")


def start_engine():
    global engine_running

    if not engine_running:
        scheduler.add_job(simulate_activity, "interval", seconds=10)
        scheduler.start()
        engine_running = True


def pause_engine():
    global engine_running

    scheduler.pause()
    engine_running = False


def resume_engine():
    global engine_running

    scheduler.resume()
    engine_running = True