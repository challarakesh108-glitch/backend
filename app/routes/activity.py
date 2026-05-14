from fastapi import APIRouter
from app.scheduler import start_engine, pause_engine, resume_engine

router = APIRouter(prefix="/activity", tags=["Activity Engine"])


@router.post("/start")
def start():
    start_engine()
    return {"message": "Automation started"}


@router.post("/pause")
def pause():
    pause_engine()
    return {"message": "Automation paused"}


@router.post("/resume")
def resume():
    resume_engine()
    return {"message": "Automation resumed"}