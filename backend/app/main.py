from fastapi import FastAPI

from .database import engine
from .models import Base

Base.metadata.create_all(engine)

app = FastAPI(title="WG Cook")


@app.get("/api/v1/health")
def health():
    return {"status": "ok"}
