from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Base


class ORMService:
    
    def __init__(self):
        self.engine = create_engine('postgresql+psycopg2://postgres:password@localhost/postgres', echo=True)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create_tables(self):
        Base.metadata.create_all(bind=self.engine)

    def insert_data(self, data):
        self.session.add(data)
        self.session.commit()

