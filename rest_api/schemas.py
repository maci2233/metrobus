from pydantic import BaseModel

class MetrobusBase(BaseModel):
    id_metrobus: int
    delegation: str
    latitude: float
    longitude: float

class MetrobusCreate(MetrobusBase):
    pass

class Metrobus(MetrobusBase):
    id: int

    class Config:
        orm_mode = True