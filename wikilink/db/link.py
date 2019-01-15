from sqlalchemy import Column, Integer, String, DateTime, text, ForeignKey
from base import Base

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
