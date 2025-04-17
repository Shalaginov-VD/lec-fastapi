from fastapi import FastAPI, HTTPException, Depends, File, Form, UploadFile
from database import get_db
from sqlalchemy.orm import Session
import models as m
from typing import List
import pyd
import shutil
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount('/files', StaticFiles(directory='files'), name='files')

@app.get('/product', response_model = List[pyd.SchemaProduct])
def get_all_product(db: Session = Depends(get_db)):
    products = db.query(m.Product).all()
    return products

@app.post('/product/image/{product_id}', response_model=pyd.SchemaProduct)
def upload_image(product_id: int, image: UploadFile, db: Session = Depends(get_db)):
    product_db = (
        db.query(m.Product).filter(m.Product.id == product_id).first()
    )
    if not product_db:
        raise HTTPException(404)
    if image.content_type not in ('image/png', 'image/jpeg'):
        raise HTTPException(400, 'Неверный тип данных')
    with open(f'files{image.filename}', 'wb') as f:
        shutil.copyfileobj(image.file, f)
    product_db.img = f'files/{image.filename}'
    db.commit()
    return product_db

@app.get('/film', response_model = List[pyd.BaseFilm])
def get_all_film(db: Session = Depends(get_db)):
    films = db.query(m.Film).all()
    return films

@app.get('/product/{product_id}', response_model = pyd.BaseProduct)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(m.Product).filter(
        m.Product.id == product_id
    ).first()
    if not product:
        raise HTTPException(404, 'Товар не найден')
    return product

@app.get('/film/{film_id}', response_model = pyd.BaseFilm)
def get_film(film_id: int, db: Session = Depends(get_db)):
    film = db.query(m.Film).filter(
        m.Film.id == film_id
    ).first()
    if not film:
        raise HTTPException(404, 'Фильм не найден')
    return film

@app.post('/product', response_model = pyd.BaseProduct)
def create_product(product: pyd.CreateProduct, db: Session = Depends(get_db)):
    product_db = db.query(m.Product).filter(m.Product.name == product.name).first()
    if product_db:
        raise HTTPException(400, 'Такой товар есть')
    
    product_db = m.Product()
    product_db.name = product.name

    db.add(product_db)
    db.commit()
    return product_db

@app.post('/film', response_model = pyd.BaseFilm)
def create_film(film: pyd.CreateFilm, db: Session = Depends(get_db)):
    film_db = db.query(m.Film).filter(m.Film.name == film.name).first()
    if film_db:
        raise HTTPException(400, 'Такой фильм есть')
    
    film_db = m.Film()
    film_db.name = film.name
    film_db.rating = film.rating

    db.add(film_db)
    db.commit()
    return film_db

@app.delete('/product/{product_id}')
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(m.Product).filter(m.Product.id == product_id).first()
    if not product:
        raise HTTPException(404, 'Товар не найден')
    db.delete(product)
    db.commit()
    return {'msg': 'Товар удален'}

@app.delete('/film/{film_id}')
def delete_film(film_id: int, db: Session = Depends(get_db)):
    film = db.query(m.Film).filter(m.Film.id == film_id).first()
    if not film:
        raise HTTPException(404, 'Фильм не найден')
    db.delete(film)
    db.commit()
    return {'msg': 'Фильм удален'}