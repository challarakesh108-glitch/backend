# Automated Email Engagement & Activity Distribution System

## Overview

This backend system simulates realistic email communication between multiple accounts.

Features:
- Account management
- Automated email activity engine
- Dynamic sender/receiver rotation
- Positive reply simulation
- Reputation tracking
- Logs & analytics APIs

## Tech Stack

- FastAPI
- Python
- SQLAlchemy
- SQLite (can switch to PostgreSQL)
- APScheduler

## Setup

```bash
pip install -r requirements.txt
python -m uvicorn app.main:app --reload