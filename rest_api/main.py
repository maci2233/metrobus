from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from crud import get_metrobuses, get_metrobus_by_id_metrobus
from models import Metrobus, Base
from schemas import Metrobus as MetrobusSchema
from database import SessionLocal, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello world"}


@app.get("/metrobuses/", response_model=List[MetrobusSchema])
async def getMetrobuses(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    metrobuses = get_metrobuses(db, skip=skip, limit=limit)
    return metrobuses

@app.get("/metrobuses/{id_metrobus}/", response_model=List[MetrobusSchema])
async def getMetrobuses(id_metrobus: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    metrobuses = get_metrobus_by_id_metrobus(db, id_metrobus=id_metrobus, skip=skip, limit=limit)
    return metrobuses