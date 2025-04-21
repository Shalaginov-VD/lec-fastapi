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

@app.post('/movie/image/{movie_id}', response_model=pyd.SchemaMovie)
def upload_image(movie_id: int, image: UploadFile, db: Session = Depends(get_db)):
    movie_db = (
        db.query(m.Movie).filter(m.Movie.id == movie_id).first()
    )
    if not movie_db:
        raise HTTPException(404)
    if image.content_type not in ('image/png', 'image/jpeg'):
        raise HTTPException(400, 'Неверный тип данных')
    with open(f'files{image.filename}', 'wb') as f:
        shutil.copyfileobj(image.file, f)
    movie_db.img = f'files/{image.filename}'
    db.commit()
    return movie_db

@app.get('/movies', response_model = List[pyd.BaseMovie])
def get_all_movies(db: Session = Depends(get_db)):
    movies = db.query(m.Movie).all()
    return movies

@app.get('/movies/{id}', response_model = pyd.BaseMovie)
def get_movie(id: int, db: Session = Depends(get_db)):
    movie = db.query(m.Movie).filter(
        m.Movie.id == id
    ).first()
    if not movie:
        raise HTTPException(404, 'Фильм не найден')
    return movie

@app.post('/movies', response_model = pyd.BaseMovie)
def create_movie(movie: pyd.CreateMovie, db: Session = Depends(get_db)):
    movie_db = db.query(m.Movie).filter(m.Movie.name == movie.name).first()
    if movie_db:
        raise HTTPException(400, 'Такой фильм есть')
    
    movie_db = m.Movie()
    movie_db.name = movie.name
    movie_db.rating = movie.rating

    db.add(movie_db)
    db.commit()
    return movie_db

@app.delete('/movies/{id}')
def delete_movie(id: int, db: Session = Depends(get_db)):
    movie = db.query(m.Movie).filter(m.Movie.id == id).first()
    if not movie:
        raise HTTPException(404, 'Фильм не найден')
    db.delete(movie)
    db.commit()
    return {'msg': 'Фильм удален'}