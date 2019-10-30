from sqlalchemy import Column, Integer, String, DateTime
from models.base import Base
import datetime


class Artist(Base):
    __tablename__ = 'artist'

    id = Column(Integer, primary_key=True)
    tag = Column(String)
    artist_rank = Column(String)
    artist_mbid = Column(String)
    artist_name = Column(String)
    streamable = Column(String)
    url = Column(String)
    inserted_date = Column(DateTime(), default=datetime.datetime.now)

    def __repr__(self):
        return "<Artist (tag='%s', artist_rank='%s', artist_mbid='%s', artist_name='%s', streamable='%s', url='%s', inserted_date='%s' )" % (self.tag, self.artist_rank, self.artist_mbid, self.artist_name, self.streamable, self.url, self.inserted_date)
