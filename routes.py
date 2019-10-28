from flask import Blueprint
from db import DB
from models.artist import Artist
from middlewares.serializer import serialize

db_obj = DB()

api = Blueprint("api", __name__, url_prefix="/api")

@api.route("/artists")

def artists():
    db_session = db_obj.get_db()
    artists = db_session.query(Artist).all()
    return serialize(artists)
