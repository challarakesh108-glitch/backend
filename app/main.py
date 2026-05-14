from fastapi import FastAPI
from app.database import Base, engine
from app.routes import accounts, activity, logs, analytics
from app import models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Email Engagement Simulator")

app.include_router(accounts.router)
app.include_router(activity.router)
app.include_router(logs.router)
app.include_router(analytics.router)


@app.get("/")
def root():
    return {"message": "Backend Running Successfully"}