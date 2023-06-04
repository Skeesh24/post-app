from .database import Base
from sqlalchemy import ClauseElement, DateTime, func, text, Boolean, Column, Integer, Row, String, Table, Tuple
from .database import metadata
from sqlalchemy.sql.elements import True_


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default="1")
    created_at = Column(DateTime(timezone=True),
                        nullable=False, server_default=text("CURRENT_TIMESTAMP()"))

    def __repr__(self) -> str:
        return f'Post №{self.id}, {self.title}, {self.content}, {self.published}'

    @staticmethod
    def dictFromRow(post: Row):
        return dict(zip(post._fields, post.tuple()))


posts = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String(50), nullable=False),
    Column("content", String(50), nullable=False),
    Column("published", Boolean, server_default="1", nullable=False),
    Column("created_at", DateTime(timezone=True),
           nullable=False, server_default=func.now())
)
