from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from src import settings

Base = declarative_base()

class Link(Base) :
    """ Generating database 'find_link' with table 'link'

               Table 'find-link'.'link
           +--------------    +--------------+------+
           | Field            | Type	      | Key  |
           +------------------|--------------+------+
           | id	           | int(11)      | pri  |
           | from_page_id     | int(11)      |      |
           | to_page_id       | int(11)      |      |
             no_of_separation | int(11)      |      |
           +--------+-------------------------------+

    """
    __tablename__ = 'link'

    id = Column(Integer(), primary_key=True)
    from_page_id = Column(Integer())
    to_page_id = Column(Integer())
    number_of_separation = Column(Integer())

    def __repr__(self):
        return "Link(from_page_id = '{self.from_page_id}'," \
                "to_page_id = '{self.to_page_id}', "\
                "number_of_separation = '{self.number_of_separation})".format(self=self)


class Page(Base) :
    """ Generating database 'find-link' with table 'page'

                   Table 'find_link'.'pages'
               +--------+--------------+------+
               | Field  | Type	        | Key  |
               +--------|--------------+------+
               | id	 | int(11)      | pri  |
               | url	 | varchar(255) |      |
               +--------+---------------------+

    """

    __tablename__ = 'page'

    id = Column(Integer(), primary_key=True)
    url = Column(String(225))

    def __repr__(self):
        return "Page(url = '{self.from_page_id})".format(self=self)

Base.metadata.create_all(settings.engine)
