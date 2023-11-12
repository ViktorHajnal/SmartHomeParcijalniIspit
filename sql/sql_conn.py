from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class Sql:
    def __init__(self) -> None:        
        self.DATABASE_URL= "sqlite:///smart_home.db"
        self.engine = create_engine(self.DATABASE_URL)
        self.Session = sessionmaker(bind=self.engine)
        
    def session(self):        
        session = self.Session()
        return session
    
    def close_session(self):
        return self.engine.dispose()
    
    