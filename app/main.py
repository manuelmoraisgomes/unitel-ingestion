from fastapi import FastAPI
from app.api.logs import router as logs_router
from app.core.database import Base, engine

app = FastAPI(title="UNITEL Ingestion")

Base.metadata.create_all(bind=engine)

app.include_router(logs_router)

@app.get("/health")
def health():
    return {"status": "ok"}


