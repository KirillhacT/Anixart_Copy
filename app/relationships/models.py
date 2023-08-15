from sqlalchemy import Column, Float, Integer, DateTime, Date, String, Text, CheckConstraint, Null, ForeignKey
from app.database import Base

class Post_genres(Base):
    __tablename__ = "post_genres"
    id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    genre_id = Column(Integer, ForeignKey('genre.id'))

class Post_voiceover(Base):
    __tablename__ = "post_voiceover"
    id = Column(Integer, primary_key=True, autoincrement=True)
    post_id = Column(Integer, ForeignKey('post.id'))
    voiceover_id = Column(Integer, ForeignKey('voiceover.id'))