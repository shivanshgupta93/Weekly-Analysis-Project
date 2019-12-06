from sqlalchemy import Column, Integer, String, Date
from models.base import Base
import datetime


class Album(Base):
    __tablename__ = 'album'

    id = Column(Integer, primary_key=True)
    tag = Column(String)
    album_rank = Column(String)
    album_name = Column(String)
    album_mbid = Column(String)
    artist_name = Column(String)
    artist_mbid = Column(String)
    artist_url = Column(String)
    url = Column(String)
    inserted_date = Column(Date(), default=datetime.datetime.now().date())

    def __repr__(self):
        return "<Album (tag='%s',album_rank='%s',album_name ='%s',album_mbid ='%s',artist_name='%s',artist_mbid='%s',artist_url='%s',url='%s', inserted_date='%s' )" % (self.tag, self.album_rank, self.album_name, self.album_mbid, self.artist_name, self.artist_mbid, self.artist_url, self.url, self.inserted_date)
