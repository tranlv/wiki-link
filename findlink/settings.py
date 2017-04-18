from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

username = "sample"
password = "sample"
ip = "localhost"
port = 3310
engine = create_engine("mysql+pymysql://'%s':'%s'@'%s':'%s'" % (
                     username, password, ip, port))
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
Base = declarative_base()
