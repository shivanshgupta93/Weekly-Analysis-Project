from sqlalchemy import Column, Integer, String, DateTime
from models.base import Base
import datetime


class Track(Base):
    __tablename__ = 'track'

    id = Column(Integer, primary_key=True)
    tag = Column(String)
    track_rank = Column(String)
    track_name = Column(String)
    track_mbid = Column(String)
    track_duration = Column(Integer)
    artist_name = Column(String)
    artist_mbid = Column(String)
    artist_url = Column(String)
    streamable = Column(String)
    url = Column(String)
    inserted_date = Column(DateTime(), default=datetime.datetime.now)

    def __repr__(self):
        return "<Track (tag='%s',track_rank='%s',track_name ='%s',track_mbid ='%s',track_duration='%s',artist_name='%s',artist_mbid='%s',artist_url='%s',streamable='%s',url='%s', inserted_date='%s' )" % (self.tag, self.track_rank, self.track_name, self.track_mbid, self.track_duration, self.artist_name, self.artist_mbid, self.artist_url, self.streamable, self.url, self.inserted_date)
