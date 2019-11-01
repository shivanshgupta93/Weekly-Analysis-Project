from sqlalchemy import Column, Integer, String, DateTime
from models.base import Base
import datetime


class Tag(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    tag = Column(String)
    inserted_date = Column(DateTime(), default=datetime.datetime.now)

    def __repr__(self):
        return "<Artist (tag='%s', inserted_date='%s' )" % (self.tag, self.inserted_date)
