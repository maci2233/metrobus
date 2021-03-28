from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer

Base = declarative_base()

class Metrobus(Base):
    __tablename__ = "Metrobus"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    mayor = Column(String)