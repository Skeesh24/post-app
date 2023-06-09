from .database import Base
from sqlalchemy import DateTime, ForeignKey, func, text, Boolean, Column, Integer, Row, String, Table
from .database import metadata
from sqlalchemy.orm import relationship


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(String(200), nullable=False)
    published = Column(Boolean, server_default="1")
    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(DateTime(timezone=True),
                        nullable=False, server_default=text("CURRENT_TIMESTAMP()"))
    # creator = relationship("User", lazy=True)

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
    Column("content", String(200), nullable=False),
    Column("published", Boolean, server_default="1", nullable=False),
    Column("user_id", Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False),
    Column("created_at", DateTime(timezone=True),
           nullable=False, server_default=func.now()),
    # Column('creator', table="users")
)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True),
                        nullable=False, server_default=text("CURRENT_TIMESTAMP()"))


users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("email", String(50), unique=True, nullable=False),
    Column("password", String(100), nullable=False),
    Column("created_at", DateTime(timezone=True),
           nullable=False, server_default=func.now())
)


class Vote(Base):
    __tablename__ = "votes"
    post_id = Column(Integer, ForeignKey(
        "posts.id", ondelete="CASCADE"), primary_key=True)
    user_id = Column(Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), primary_key=True)


votes = Table(
    "votes",
    metadata,
    Column("post_id", Integer, ForeignKey(
        "posts.id", ondelete="CASCADE"), primary_key=True),
    Column("user_id", Integer, ForeignKey(
        "users.id", ondelete="CASCADE"), primary_key=True),
)
