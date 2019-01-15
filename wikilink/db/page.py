from sqlalchemy import Column, Integer, String, DateTime, text, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from base import Base

class Page(Base):
	__tablename__ = 'page'

	id = Column(Integer(), primary_key=True)
	url = Column(LONGTEXT)
	created = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))

	def __repr__(self):
		return "<Page(page_id = '%s', url ='%s', created='%s')>" % (self.page_id, self.url, self.created)