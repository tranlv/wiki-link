from sqlalchemy import Column, Integer, String, DateTime, text
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite://', echo=True)
Base = declarative_base()
Base.metadata.create_all(engine)
session = Session(engine)


class Link(Base):
    __tablename__ = 'links'
    id = Column(Integer, primary_key=True)
    from_page_id = Column(Integer)
    to_page_id = Column(Integer)
    number_of_separation = Column(Integer,nullable=False)
    created = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))

    def __repr__(self):
        return "<Link(from_page_id='%s', to_page_id='%s', number_of_separation='%s', created='%s')>" % (
                     self.from_page_id, self.to_page_id, self.number_of_separation, self.created)


class Page(Base) :
    __tablename__ = 'pages'
    id = Column(Integer(), primary_key=True)
    url = Column(String(225))
    created = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))

    def __repr__(self):
        return "<Page(url ='%s', created='%s')>" %(self.url, self.created)

