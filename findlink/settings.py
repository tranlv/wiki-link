from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine  = create_engine('mysql+pymysql://root:13061990@localhost:32782', pool_recycle=3600)
Session = sessionmaker(bind=engine)
session = Session()
