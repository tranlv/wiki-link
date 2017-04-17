from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine  = create_engine('mysql+pymysql://username:password@ip:port', pool_recycle=3600)
Session = sessionmaker(bind=engine)
session = Session()
