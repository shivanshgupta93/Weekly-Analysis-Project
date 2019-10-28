from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import os


class DB:
    __session = None

    def __init__(self):
        if not DB.__session:
            DB.__session = self.create_db_session()

    def create_db_session(self):
        env = os.environ.get("env", "development")
        engine = None
        if env == "development":
            engine = create_engine("sqlite:///music.db", echo = True, connect_args={'check_same_thread': False}) #sqlite

        elif env == "production":
            db_uri = os.environ.get("DATABASE_URL", "")
            engine = create_engine(db_uri) #postgres
            meta = MetaData()
            meta.create_all(engine)
        else:
            raise Exception("environment not available")

        Session = sessionmaker(bind = engine)
        session = Session()

        return session

    def get_db(self):
        return DB.__session

    def close(self):
        DB.__session.close()