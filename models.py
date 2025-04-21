from database import Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key = True, autoincrement = True)
    title = Column(String(255), unique = True, nullable = False)
    year = Column(Integer)
    genre_id = Column(Integer, ForeignKey('genres.id'))
    duration = Column(Float)
    rating = Column(Float(10))
    description = Column(String(255), nullable = True)
    poster = Column(String(255), nullable = True)
    created_at = Column(DateTime, default=datetime.utcnow)

class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key = True, autoincrement = True)
    title = Column(String(255), unique = True, nullable = False)
    description = Column(String(255), nullable = True)
    movies = relationship('Movie', backref = 'genres')