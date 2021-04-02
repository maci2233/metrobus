from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from crud import get_metrobuses, get_metrobus_by_id_metrobus, get_metrobus_by_delegation
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
    return {"message": "Metrobus Root page, go to /docs to read the swagger REST API documentation"}


@app.get("/metrobuses/", response_model=List[MetrobusSchema])
async def get_all_metrobuses(db: Session = Depends(get_db)):
    """
    Get the list of all metrobuses
    """
    metrobuses = get_metrobuses(db)
    return metrobuses


@app.get("/metrobuses/delegaciones-activas/")
async def get_active_delegations(db: Session = Depends(get_db)):
    """
    Get the list of all delegations in the DB
    If a delegation exists, that means a metrobus has gone through it
    """
    delegations = set(r.delegation for r in get_metrobuses(db))
    return delegations


@app.get("/metrobuses/{id_metrobus}/", response_model=List[MetrobusSchema])
async def get_metrobus_registers_based_on_id_metrobus(id_metrobus: int, db: Session = Depends(get_db)):
    """
    Get all the registers for a specific metrobus using the metrobus id.
    For example if a metrobus has appear 3 times at different locations, then the response should contain details of those locations.
    """
    metrobuses = get_metrobus_by_id_metrobus(db, id_metrobus=id_metrobus)
    return metrobuses


@app.get("/metrobuses/delegacion/{delegation_name}/", response_model=List[MetrobusSchema])
async def get_metrobuses_based_on_delegation_name(delegation_name: str, db: Session = Depends(get_db)):
    """
    Get the list of all metrobuses that have been at a given delegation.
    """
    metrobuses = get_metrobus_by_delegation(db, delegation_name=delegation_name)
    return metrobuses