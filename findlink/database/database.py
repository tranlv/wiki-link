from sqlalchemy import Column, Integer, String, DateTime, text
from findlink.settings import Base, engine


class Link(Base):

    """ Generating database 'find_link' with table 'link'

               Table 'find-link'.'link
           +--------------    +--------------+------+
           | Field            | Type	       Key  |
           +------------------|--------------+------+
           | id	              | int           | pri  |
           | from_page_id     | int           |      |
           | to_page_id       | int           |      |
           | no_of_separation | int           |      |
           | created          | timestamp
           +--------+-------------------------------+
    """

    __tablename__ = 'links'

    id = Column(Integer(), primary_key=True)
    from_page_id = Column(Integer())
    to_page_id = Column(Integer())
    number_of_separation = Column(Integer(),nullable=False)
    created = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))

    def __repr__(self):
        return "<Link(from_page_id='%s', to_page_id='%s', number_of_separation='%s', created='%s')>" % (
                     self.from_page_id, self.to_page_id, self.number_of_separation, self.created)


class Page(Base) :
    """ Generating database 'find-link'.'pages'

                   Table 'find_link'.'pages'
               +--------+--------------+------+
               | Field  | Type	       | Key  |
               +--------|--------------+------+
               | id	    | int          | pri  |
               | url	| varchar(255) |      |
               | created | timestamp
               +--------+---------------------+
    """

    __tablename__ = 'pages'

    id = Column(Integer(), primary_key=True)
    url = Column(String(225))
    created = Column(DateTime, nullable=False, server_default=text('CURRENT_TIMESTAMP'))

    def __repr__(self):
        return "<Page(url ='%s', created='%s')>" %(self.url, self.created)

Base.metadata.create_all(engine)
