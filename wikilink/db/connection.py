#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Provide Connection - the main gateway to access db"""

# third-party modules
from sqlalchemy import create_engine
from sqlalchemy_utils import functions

# own modules
from .base import Base

__author__ = "Tran Ly Vu (vutransingapore@gmail.com)"
__copyright__ = "Copyright (c) 2016 - 2019 Tran Ly Vu. All Rights Reserved."
__credits__ = ["Tranlyvu"]
__license__ = "Apache License 2.0"
__maintainer__ = "Tran Ly Vu"
__email__ = "vutransingapore@gmail.com"
__status__ = "Production"

class Connection:
	def __init__(self, db, name, password, ip, port):
		
		if db == "postgresql":
			connection = "postgresql+psycopg2://" + name + ":" \
			              + password + "@" + ip + ":" + port			
		elif db == "mysql":
			connection = "mysql://" + name + ":" + password \
			              + "@" + ip + ":" + port
		else:
			raise ValueError("db type only \
				support \"mysql\" or \"postgresql\" argument.")
		
		db_name = 'wikilink'
		# Turn off echo
		self.engine = create_engine(connection + "/" + db_name + '?charset=utf8'
									,echo=False, encoding='utf-8' 
									,pool_pre_ping=True 
									,pool_size=10)

		if not functions.database_exists(self.engine.url):
			functions.create_database(self.engine.url)

		# If table don't exist, Create.
		if (not self.engine.dialect.has_table(self.engine, 'link')\
			and not self.engine.dialect.has_table(self.engine, 'page')):
			
			Base.metadata.create_all(self.engine)
