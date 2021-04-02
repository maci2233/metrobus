from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Float

Base = declarative_base()

class Metrobus(Base):
    """
    Metrobus class used by the ORM to map it with the Metrobus table in the DB
    """
    __tablename__ = "Metrobus"
    id = Column(Integer, primary_key=True)
    id_metrobus = Column(Integer)
    delegation = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)