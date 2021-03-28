from sqlalchemy.orm import Session

from models import Metrobus


def get_metrobus(db: Session, metrobus_id: int):
    return db.query(Metrobus).filter(Metrobus.id == metrobus_id).first()

def get_metrobuses(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(Metrobus).offset(skip).limit(limit).all()