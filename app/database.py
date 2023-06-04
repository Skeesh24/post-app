from time import sleep
from sqlalchemy import create_engine, text
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from mysql.connector import connect


from app.config import Config


engine = create_engine(url=Config.MYSQL_CONNECTION_STRING)

LocalSession = sessionmaker(bind=engine, autoflush=False)

LocalSession().execute(
    text(f"CREATE DATABASE IF NOT EXISTS {Config.MYSQL_DATABASE}"))
LocalSession().execute(text(f"USE {Config.MYSQL_DATABASE}"))

engine = create_engine(
    url=Config.MYSQL_CONNECTION_STRING+f"/{Config.MYSQL_DATABASE}")

LocalSession = sessionmaker(bind=engine, autoflush=False)

Base = declarative_base()

metadata = MetaData()


def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()


cursor = None
connection = None
