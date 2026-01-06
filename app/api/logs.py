from app.schemas.logs import LogCreate
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.logs import LogCreate
from app.models.logs import Log
from app.core.database import SessionLocal

router = APIRouter(prefix="/logs", tags=["Logs"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def ingest_log(log: LogCreate, db: Session = Depends(get_db)):
    entry = Log(**log.dict())
    db.add(entry)
    db.commit()
    return {"status": "stored"}

