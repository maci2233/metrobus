from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Base


class ORMService:
    
    def __init__(self):
        """
        ORMService Constructor.
        Create an engine that connects to the postgres DB and start a Session used for DB petitions.
        """
        self.engine = create_engine('postgresql+psycopg2://postgres:password@db/postgres', echo=True)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def create_tables(self):
        """
        Create all tables (if they do not exist in the DB) that extend the Base SqlAlchemy class
        """
        Base.metadata.create_all(bind=self.engine)

    def insert_data(self, data):
        """
        Insert a record into the DB
        
        params: 
            - data(string): Instance of a class(must extend Base SQLAlchemy class) that will be inserted in the DB.
        """
        self.session.add(data)
        self.session.commit()

