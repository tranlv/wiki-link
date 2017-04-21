from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base


class Setting:

	def __init__(self):
		engine = create_engine('sqlite://', echo=True)
		self.Base = declarative_base()
		self.Base.metadata.create_all(engine)
		self.session = Session(engine)

