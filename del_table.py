from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from meteo.meteo import Base, MeteoInfo


DATABASE_URL= "sqlite:///smart_home.db"

engine = create_engine('sqlite:///smart_home.db')  
Session = sessionmaker(bind=engine)
session = Session()

table_name = MeteoInfo.__tablename__
MeteoInfo.__table__.drop(engine)

