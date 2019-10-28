from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime
import datetime

def track(db, track):
    meta = MetaData()
    track_table = Table('track', meta,
    Column('id',Integer, primary_key = True),
    Column('tag', String),
    Column('track_rank', String),
    Column('track_name', String),
    Column('track_mbid', String),
    Column('track_duration', Integer),
    Column('artist_name', String),
    Column('artist_mbid', String),
    Column('artist_url', String),
    Column('streamable',String),
    Column('url', String),
    Column('inserted_date', DateTime(), default = datetime.datetime.now)
    )

    track_table.create(db, checkfirst=True)

    track_ins = track_table.insert(None).values(track)
    con = db.connect()
    result = con.execute(track_ins)

    return result


