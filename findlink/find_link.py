from data_handle import DataHandle
from searcher import Searcher
from sqlalchemy import Column, Integer, String, DateTime, text, ForeignKey
from findlink import engine,Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base() #metadata

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



class FindLink:
    def __init__(self, starting_url, ending_url, limit = 6):
        session = Session()

        Base.metadata.create_all(bind=engine)
        self.limit = limit
        self.starting_url = starting_url
        self.ending_url = ending_url
        self.found = False
        self.number_of_separation = 1
        DataHandle().update_page_if_not_exists(starting_url)
        DataHandle().update_page_if_not_exists(ending_url)

        # update link for starting_page
        starting_id = session.query(Page.id).filter(Page.url == starting_url).all()
        DataHandle.update_link(starting_id[0], starting_id[0], 0)

    def search(self):

        self.found = DataHandle().retrieve_data(self.ending_url, self.number_of_separation)

        while self.found is False:
            self.number_of_separation += 1
            if self.number_of_separation > self.limit:
                print ("Number of separation is exceeded number of limit. Stop searching!")
                return
            self.found = DataHandle().retrieve_data(self.ending_url, self.number_of_separation)

        print ("Smallest number of separation is " + str(self.number_of_separation))

    def print_links(self):

        if self.number_of_separation > self.limit or self.found is False:
            print ("No solution within limit!")
            return
        my_search = Searcher(self.starting_url, self.ending_url)
        my_list = [self.ending_page] + my_search.list_of_links()
        my_list.reverse()

        for x in my_list:
            print x


