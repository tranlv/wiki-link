from sqlalchemy import create_engine
from sqlalchemy_utils import functions
from sqlalchemy.orm import sessionmaker

class DB:
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