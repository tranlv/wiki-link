from sqlalchemy import Column, Integer, String, DateTime, text, ForeignKey, func, create_engine
from sqlalchemy.ext.declarative import declarative_base
import configparser
import re
from requests import get, HTTPError
from bs4 import BeautifulSoup
from sqlalchemy.orm import sessionmaker


Base = declarative_base() #metadata

def get_database_url():
    config = configparser.ConfigParser()
    config.read('wiki-link.conf')
    return config.get('database', 'connection')


class Link(Base):
    __tablename__ = 'links'

    id = Column(Integer, primary_key=True)
    from_page_id = Column(Integer, ForeignKey('Page.id'))
    to_page_id = Column(Integer, ForeignKey('Page.id'))
    number_of_separation = Column(Integer,nullable=False)
    created = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))

    def __repr__(self):
        return "<Link(from_page_id='%s', to_page_id='%s', number_of_separation='%s', created='%s')>" % (
                     self.from_page_id, self.to_page_id, self.number_of_separation, self.created)

class Page(Base):
    __tablename__ = 'pages'

    id = Column(Integer(), primary_key=True)
    url = Column(String(225))
    created = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))

    def __repr__(self):
        return "<Page(url ='%s', created='%s')>" %(self.url, self.created)

def main():
    NEW_DB_NAME = 'wikilink'
    DB_CONN_FORMAT = get_database_url() + "/" + NEW_DB_NAME
    engine = create_engine(DB_CONN_FORMAT)

if __name__ == "__main__": main()

