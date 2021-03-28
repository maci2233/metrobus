from sqlalchemy.orm import Session

from models import Metrobus


def get_metrobus(db: Session, id: int):
    return db.query(Metrobus).filter(Metrobus.id == id).first()

def get_metrobus_by_id_metrobus(db: Session, id_metrobus: str, skip: int = 0, limit: int = 100):
    return db.query(Metrobus).filter(Metrobus.id_metrobus == id_metrobus).offset(skip).limit(limit).all()

def get_metrobuses(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(Metrobus).offset(skip).limit(limit).all()