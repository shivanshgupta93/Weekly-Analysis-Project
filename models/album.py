from sqlalchemy import  Column, Integer, String, DateTime
from models.base import Base 
import datetime

class Album(Base):
    __tablename__ = 'albums'

    id = Column(Integer, primary_key = True)
    tag = Column(String)
    album_rank = Column(String)
    album_name = Column(String)
    album_mbid = Column(String)
    artist_name = Column(String)
    artist_mbid = Column(String)
    artist_url = Column(String)
    url = Column(String)
    inserted_date = Column(DateTime(), default = datetime.datetime.now)

    '''def __repr__(self):
        return "<Album (tag='%s', album_rank='%s', album_name ='%s', artist_mbid='%s', artist_name='%s', streamable='%s', url='%s', inserted_date='%s' )" 
        % (self.tag, self.artist_rank, self.artist_mbid, self.artist_name, self.streamable, self.url, self.inserted_date)'''