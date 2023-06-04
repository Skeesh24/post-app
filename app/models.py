from typing import Any
from .database import Base
from sqlalchemy import Boolean, Column, Integer, Row, String, Table
from .database import metadata


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=True)

    def __repr__(self) -> str:
        return f'Post #{self.id}, {self.title}, {self.content}, {self.published}'

    @staticmethod
    def getInstanceFromRow(post: Row[Any]):
        return Post(**dict(zip(post._fields, post.tuple())))


posts = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50), nullable=False),
    Column("content", String(50), nullable=False),
    Column("published", Boolean, nullable=False),
)
