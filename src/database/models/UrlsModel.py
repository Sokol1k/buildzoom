from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base


class UrlsModel(declarative_base()):
    __tablename__ = 'urls'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    url = Column('url', String, nullable=False, unique=True, index=True)
    status = Column('status', Integer, nullable=False)
