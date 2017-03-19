from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declation import declarative_base



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
        return "Linl"
