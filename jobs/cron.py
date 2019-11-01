import os
import requests
from consts import *
from db import DB
from models.artist import Artist
from models.album import Album
from models.track import Track
from models.tag import Tag
from middlewares.deserializer import deserializer

db_obj = DB()
db_session = db_obj.get_db()

run_cron = int(os.environ.get("run_cron_job", 1))

def cron_job():
    if run_cron == 1:
        tags_payload = {
            "method": "tag.getTopTags",
            "api_key": API_KEY,
            "format": "json"    
        }
        top_tags = deserializer(requests.get(BASE_URL, params=tags_payload))
        tags_lst = top_tags['toptags']['tag']
        db_session.add_all(
                            [Tag(tag=next_item['name']) 
                            for next_item in tags_lst[:10]]
                        )
        db_session.commit()

        for key,value in MUSIC.items():
            for item in tags_lst[:10]:
                payload = {
                    "method": value,
                    "tag": item['name']
                    ,"api_key": API_KEY,
                    "format": "json"
                    }
                    
                top = deserializer(requests.get(BASE_URL, params=payload))
                
                if key == "artist":
                    first_key = "top" + key + "s"
                    top_item = top[first_key][key]
                    db_session.add_all(
                            [Artist(tag=item['name'], artist_rank = next_item['@attr']['rank'], artist_mbid = next_item.get('mbid','None'),
                            artist_name = next_item['name'], streamable = next_item['streamable'], url = next_item['url']) 
                            for next_item in top_item[:20]]
                        )

                if key == "album":
                    first_key = key + "s"
                    top_item = top[first_key][key]
                    db_session.add_all(
                            [Album(tag=item['name'], album_rank = next_item['@attr']['rank'], album_name = next_item['name'], 
                            album_mbid=next_item.get('mbid','None'), artist_name = next_item['artist']['name'], 
                            artist_mbid = next_item['artist'].get('mbid','None'),
                            artist_url = next_item['artist']['url'], url = next_item['url']) 
                            for next_item in top_item[:20]]
                        )

                if key == "track":
                    first_key = key + "s"
                    top_item = top[first_key][key]
                    db_session.add_all(
                            [Track(tag=item['name'], track_rank = next_item['@attr']['rank'], track_name = next_item['name'], 
                            track_mbid=next_item.get('mbid','None'), track_duration=int(next_item.get('duration','0')),
                            artist_name = next_item['artist']['name'], 
                            artist_mbid = next_item['artist'].get('mbid','None'),
                            artist_url = next_item['artist']['url'], streamable=next_item['streamable']['fulltrack'], 
                            url = next_item['url']) 
                            for next_item in top_item[:20]]
                        )
                db_session.commit()