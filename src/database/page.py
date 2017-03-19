from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declation import declarative_base

Base = declarative_base()

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
