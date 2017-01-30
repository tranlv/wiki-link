from sqlalchemy import Column, Integer, String

class Page(Base) :
    __tablename__ = 'pages'

    id = Column(Integer, primary_key=True)
    url = Column(String)
