from pydantic import BaseModel

class MetrobusBase(BaseModel):
    name: str
    mayor: str

class MetrobusCreate(MetrobusBase):
    pass

class Metrobus(MetrobusBase):
    id: int

    class Config:
        orm_mode = True