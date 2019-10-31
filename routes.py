from flask import Blueprint
from db import DB
from models.artist import Artist
from models.album import Album
from models.track import Track
from middlewares.serializer import serialize

db_obj = DB()
db_session = db_obj.get_db()

api = Blueprint("api", __name__, url_prefix="/api")

@api.route("/artists")

def artists():
    artists = db_session.query(Artist).all()
    return serialize(artists)


@api.route("/albums")

def albums():
    albums = db_session.query(Album).all()
    return serialize(albums)


@api.route("/tracks")

def tracks():
    tracks = db_session.query(Track).all()
    return serialize(tracks)