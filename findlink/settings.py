from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

username = "abc"
password = "abc"
ip = "abc"
port = "abc"
engine = create_engine("mysql+pymysql://'%s':'%s'@'%s':'%s'", pool_recycle=3600) % (
                     username, password, ip, port)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()
