from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine  = create_engine('mysql+pymysql://username:password@ip:port', pool_recycle=3600)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
