from sqlalchemy import Column, Integer, String
from findlink.settings import Base,engine

class Link(Base) :
    """ Generating database 'find_link' with table 'link'

               Table 'find-link'.'link
           +--------------    +--------------+------+
           | Field            | Type	      | Key  |
           +------------------|--------------+------+
           | id	              | int(11)      | pri  |
           | from_page_id     | int(11)      |      |
           | to_page_id       | int(11)      |      |
             no_of_separation | int(11)      |      |
           +--------+-------------------------------+
    """

    __tablename__ = 'links'

    id = Column(Integer(), primary_key=True)
    from_page_id = Column(Integer())
    to_page_id = Column(Integer())
    number_of_separation = Column(Integer())

    def __repr__(self):
        return "<Link(from_page_id='%s', to_page_id='%s', number_of_separation='%s')>" % (
                     self.from_page_id, self.to_page_id, self.number_of_separation)

class Page(Base) :
    """ Generating database 'find-link'.'pages'

                   Table 'find_link'.'pages'
               +--------+--------------+------+
               | Field  | Type	        | Key  |
               +--------|--------------+------+
               | id	    | int(11)      | pri  |
               | url	| varchar(255) |      |
               +--------+---------------------+
    """

    __tablename__ = 'pages'

    id = Column(Integer(), primary_key=True)
    url = Column(String(225))

    def __repr__(self):
        return "<Page(url ='%s')>" %(self.url)

Base.metadata.create_all(engine)
