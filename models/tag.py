from sqlalchemy import Column, Integer, String, Date
from models.base import Base
import datetime


class Tag(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    tag = Column(String)
    inserted_date = Column(Date(), default=datetime.datetime.now().date())
    tag_rank = Column(String)

    def __repr__(self):
        return "<Artist (tag='%s', inserted_date='%s', tag_rank='%s' )" % (self.tag, self.inserted_date, self.tag_rank)
