from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer
from database import Base


class Metrobus(Base):
    __tablename__ = "Metrobus"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    mayor = Column(String)