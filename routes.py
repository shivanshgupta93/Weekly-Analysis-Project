from flask import Blueprint, request
from db import DB
from models.artist import Artist
from models.album import Album
from models.track import Track
from models.tag import Tag
from middlewares.serializer import serialize

db_obj = DB()
db_session = db_obj.get_db()

api = Blueprint("api", __name__, url_prefix="/api")

@api.route("/tags")
def tags():
    tags = db_session.query(Tag).distinct(Tag.tag)
    return serialize(tags)

@api.route("/artists")

def artists():
    id_start = request.args.get('id_start')
    id_end = request.args.get('id_end')
    tag = request.args.get('tag')
    rank = request.args.get('rank')
    if tag:
        if rank:
            if id_start:
                if id_end:
                    artists = db_session.query(Artist).filter(Artist.tag == tag, Artist.artist_rank == rank, Artist.id >= id_start, Artist.id <= id_end)
                else:
                    artists = db_session.query(Artist).filter(Artist.tag == tag, Artist.artist_rank == rank, Artist.id >= id_start)
            else:
                if id_end:
                    artists = db_session.query(Artist).filter(Artist.tag == tag, Artist.artist_rank == rank, Artist.id <= id_end)
                else:
                    artists = db_session.query(Artist).filter(Artist.tag == tag, Artist.artist_rank == rank)
        else:
            if id_start:
                if id_end:
                    artists = db_session.query(Artist).filter(Artist.tag == tag, Artist.id >= id_start, Artist.id <= id_end)
                else:
                    artists = db_session.query(Artist).filter(Artist.tag == tag, Artist.id >= id_start)
            else:
                if id_end:
                    artists = db_session.query(Artist).filter(Artist.tag == tag, Artist.id <= id_end)
                else:
                    artists = db_session.query(Artist).filter(Artist.tag == tag)

    return serialize(artists)

@api.route("/artists/all")

def all_artists():
    artists = db_session.query(Artist).all()
    return serialize(artists)

@api.route("/albums")

def albums():
    id_start = request.args.get('id_start')
    id_end = request.args.get('id_end')
    tag = request.args.get('tag')
    rank = request.args.get('rank')
    if tag:
        if rank:
            if id_start:
                if id_end:
                    albums = db_session.query(Album).filter(Album.tag == tag, Album.album_rank == rank, Album.id >= id_start, Album.id <= id_end)
                else:
                    albums = db_session.query(Album).filter(Album.tag == tag, Album.album_rank == rank, Album.id >= id_start)
            else:
                if id_end:
                    albums = db_session.query(Album).filter(Album.tag == tag, Album.album_rank == rank, Album.id <= id_end)
                else:
                    albums = db_session.query(Album).filter(Album.tag == tag, Album.album_rank == rank)
        else:
            if id_start:
                if id_end:
                    albums = db_session.query(Album).filter(Album.tag == tag, Album.id >= id_start, Album.id <= id_end)
                else:
                    albums = db_session.query(Album).filter(Album.tag == tag, Album.id >= id_start)
            else:
                if id_end:
                    albums = db_session.query(Album).filter(Album.tag == tag, Album.id <= id_end)
                else:
                    albums = db_session.query(Album).filter(Album.tag == tag)

    return serialize(albums)

@api.route("/albums/all")

def all_albums():
    albums = db_session.query(Album).all()
    return serialize(albums)

@api.route("/tracks")

def tracks():
    tracks = db_session.query(Track).all()
    return serialize(tracks)

@api.route("/tracks/all")

def all_tracks():
    tracks = db_session.query(Track).all()
    return serialize(tracks)