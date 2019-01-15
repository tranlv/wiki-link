from sqlalchemy import Column, Integer, String, DateTime, text, ForeignKey, func
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy import create_engine
from sqlalchemy_utils import functions
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()  # metadata

class Page(Base):
	__tablename__ = 'page'

	id = Column(Integer(), primary_key=True)
	url = Column(LONGTEXT)
	created = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))

	def __repr__(self):
		return "<Page(page_id = '%s', url ='%s', created='%s')>" % (self.page_id, self.url, self.created)


class Link(Base):
	__tablename__ = 'link'

	id = Column(Integer, primary_key=True)
	from_page_id = Column(Integer, ForeignKey('page.id'))
	to_page_id = Column(Integer, ForeignKey('page.id'))
	number_of_separation = Column(Integer, nullable=False)
	created = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))

	def __repr__(self):
		return "<Link(from_page_id='%s', to_page_id='%s', number_of_separation='%s', created='%s')>" % (
			self.from_page_id, self.to_page_id, self.number_of_separation, self.created)

class db:
	def __init__(self, db, name, password, ip, port):
		if db == 'postgresql':
			connection = "postgresql+psycopg2://" + name + ":" + passowrd + "@" + ip + ":" + port			
		else: 
			connection = db + "://" + name + ":" + passowrd + "@" + ip + ":" + port
		
		db_name = 'wikilink'
		# Turn off echo
		engine = create_engine(connection + "/" + db_name + '?charset=utf8', echo=False, encoding='utf-8')
		if not functions.database_exists(engine.url):
			functions.create_database(engine.url)

		self.session = sessionmaker(bind=engine)()
		# If table don't exist, Create.
		if (not engine.dialect.has_table(engine, 'link') and not engine.dialect.has_table(engine, 'page')):
			Base.metadata.create_all(engine)