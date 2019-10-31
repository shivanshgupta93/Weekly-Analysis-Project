import os
import requests
from consts import *
from db import DB
from models.artist import Artist
from models.album import Album
from models.track import Track
from middlewares.deserializer import deserializer

db_obj = DB()
db_session = db_obj.get_db()

run_cron = os.environ.get("run_cron_job", 1)
print(run_cron)

def cron_job():
    if run_cron == 1:
        tags_payload = {
            "method": "tag.getTopTags",
            "api_key": API_KEY,
            "format": "json"    
        }
        print("running cron job")
        top_tags = deserializer(requests.get(BASE_URL, params=tags_payload))
        tags_lst = top_tags['toptags']['tag']

        for key,value in MUSIC.items():
            for item in tags_lst:
                payload = {
                    "method": value,
                    "tag": item['name']
                    ,"api_key": API_KEY,
                    "format": "json"
                    }
                    
                top = deserializer(requests.get(BASE_URL, params=payload))
                ##final_lst = []
                
                if key == "artist":
                    first_key = "top" + key + "s"
                    top_item = top[first_key][key]
                    '''for next_item in top_item:
                        value_dic={
                            "tag":item['name'],
                            "artist_rank":next_item['@attr']['rank'],
                            "artist_mbid":next_item.get('mbid','None'),
                            "artist_name":next_item['name'],
                            "streamable":next_item['streamable'],
                            "url":next_item['url']
                            }

                        final_lst.append(value_dic)
                    result = artist(db, final_lst)'''
                    db_session.add_all(
                            [Artist(tag=item['name'], artist_rank = next_item['@attr']['rank'], artist_mbid = next_item.get('mbid','None'),
                            artist_name = next_item['name'], streamable = next_item['streamable'], url = next_item['url']) 
                            for next_item in top_item]
                        )
                    db_session.commit()

                if key == "album":
                    first_key = key + "s"
                    top_item = top[first_key][key]
                    '''for next_item in top_item:
                        value_dic={
                            "tag":item['name'],
                            "album_rank":next_item['@attr']['rank'],
                            "album_name":next_item['name'],
                            "album_mbid":next_item.get('mbid','None'),
                            "artist_name":next_item['artist']['name'],
                            "artist_mbid":next_item['artist'].get('mbid','None'),
                            "artist_url":next_item['artist']['url'],
                            "url":next_item['url']
                        }
                        final_lst.append(value_dic)
                    result = album(db, final_lst)'''
                    db_session.add_all(
                            [Album(tag=item['name'], album_rank = next_item['@attr']['rank'], album_name = next_item['name'], 
                            album_mbid=next_item.get('mbid','None'), artist_name = next_item['artist']['name'], 
                            artist_mbid = next_item['artist'].get('mbid','None'),
                            artist_url = next_item['artist']['url'], url = next_item['url']) 
                            for next_item in top_item]
                        )
                    db_session.commit()

                if key == "track":
                    first_key = key + "s"
                    top_item = top[first_key][key]
                    '''for next_item in top_item:
                        value_dic={
                            "tag":item['name'],
                            "track_rank":next_item['@attr']['rank'],
                            "track_name":next_item['name'],
                            "track_mbid":next_item.get('mbid','None'),
                            "track_duration":int(next_item.get('duration','0')),
                            "artist_name":next_item['artist']['name'],
                            "artist_mbid":next_item['artist'].get('mbid','None'),
                            "artist_url":next_item['artist']['url'],
                            "streamable":next_item['streamable']['fulltrack'],
                            "url":next_item['url']
                        }
                        final_lst.append(value_dic)
                    result = track(db, final_lst)'''
                    db_session.add_all(
                            [Track(tag=item['name'], track_rank = next_item['@attr']['rank'], track_name = next_item['name'], 
                            track_mbid=next_item.get('mbid','None'), track_duration=int(next_item.get('duration','0')),
                            artist_name = next_item['artist']['name'], 
                            artist_mbid = next_item['artist'].get('mbid','None'),
                            artist_url = next_item['artist']['url'], streamable=next_item['streamable']['fulltrack'], 
                            url = next_item['url']) 
                            for next_item in top_item]
                        )
                    db_session.commit()