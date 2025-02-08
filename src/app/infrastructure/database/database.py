from sqlmodel import create_engine

class DataBaseEngine():
    DATABASE_URL = "mysql+pymysql://root:facebookalec7@localhost/expensetrackerapi"
    engine = None
    
    def create_engin(cls):
        if cls.engine is None:
            cls.engine = create_engine(cls.DATABASE_URL, echo=True)