from sqlalchemy import create_engine, text
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


from ..config import Config

MYSQL_CONNECTION_STRING = f"mysql+{Config.MYSQL_DRIVER}://{Config.MYSQL_USER}:{Config.MYSQL_PASSWORD}@{Config.MYSQL_HOST}:{Config.MYSQL_PORT}"

engine = create_engine(url=MYSQL_CONNECTION_STRING)

LocalSession = sessionmaker(bind=engine, autoflush=False)

LocalSession().execute(
    text(f"CREATE DATABASE IF NOT EXISTS {Config.MYSQL_DATABASE}"))
LocalSession().execute(text(f"USE {Config.MYSQL_DATABASE}"))

engine = create_engine(
    url=MYSQL_CONNECTION_STRING+f"/{Config.MYSQL_DATABASE}")

LocalSession = sessionmaker(bind=engine, autoflush=False)

Base = declarative_base()

metadata = MetaData()


def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()
