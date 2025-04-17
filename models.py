from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(255), unique = True)

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(255), unique = True)
    category_id = Column(Integer, ForeignKey('categories.id'))
    img = Column(String(255), nullable = True)

    category = relationship('Category', backref = 'products') 

class Film(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(255), unique = True)
    rating = Column(Integer)
    