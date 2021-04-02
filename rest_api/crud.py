from sqlalchemy.orm import Session

from models import Metrobus


def get_metrobus(db: Session, id: int):
    return db.query(Metrobus).filter(Metrobus.id == id).first()

def get_metrobuses(db: Session):
    return db.query(Metrobus).all()

def get_metrobus_by_id_metrobus(db: Session, id_metrobus: str):
    return db.query(Metrobus).filter(Metrobus.id_metrobus == id_metrobus).all()

def get_metrobus_by_delegation(db, delegation_name: str):
    return db.query(Metrobus).filter(Metrobus.delegation == delegation_name).all()