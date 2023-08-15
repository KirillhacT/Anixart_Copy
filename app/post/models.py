from sqlalchemy import Column, Float, Integer, Date, String, Text, CheckConstraint, Null, ForeignKey
from app.database import Base


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, name="id", primary_key=True, autoincrement=True)
    release_date = Column(Date, name="release_date", nullable=False)
    name = Column(String(100), name="name", nullable=False)
    alternative_name = Column(String(100), name="alternative_name", nullable=False)
    studio = Column(String(50), name="studio", nullable=False)
    type = Column(String(20), name="type", nullable=False)
    status = Column(String(20), name="status", nullable=False)
    description = Column(Text, name="description", nullable=False)
    series_count = Column(Integer, name="series_count", nullable=False)
    photo_id = Column(Integer, name="photo_id")
    franchise_id = Column(Integer, ForeignKey("franchise.id"), name="franchise_id", default=Null)
    rating = Column(Float, name="rating",nullable=False)
    __table_args__ = (
        CheckConstraint(type.in_(['ТВ-сериал', 'OVA', 'ONA', 'Фильм'])),
        CheckConstraint(status.in_(["Онгоинг", "Завершенный", "Анонс"])),
    )

class Franchise(Base):
    __tablename__ = "franchise"
    id = Column(Integer, name="id", primary_key=True, autoincrement=True)
    name = Column(String(100), name="name", nullable=False)

class Genre(Base):
    __tablename__ = "genre"
    id = Column(Integer, name="id", primary_key=True, autoincrement=True)
    name = Column(String(30), name="name", nullable=False)

class Voiceover(Base):
    __tablename__ = "voiceover"
    id = Column(Integer, name="id", primary_key=True, autoincrement=True)
    name = Column(String(30), name="name", nullable=False)



    