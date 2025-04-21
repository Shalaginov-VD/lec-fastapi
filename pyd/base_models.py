from pydantic import BaseModel, Field

class BaseMovie(BaseModel):
    id: int = Field(example = 1)
    title: str = Field(example = 'Название фильма')
    year: int = Field(example = 2000)
    duration: float = Field(example = '90.2')
    rating: float = Field(example = 9.9)
    description: str = Field(example = 'Описание фильма')
    poster: str = Field(example = 'URL изображения')

class BaseGenre(BaseModel):
    id: int = Field(example = 1)
    title: str = Field(example = 'Название жанра')

# class BaseProduct(BaseModel):
#     id: int = Field(example = 1)
#     name: str = Field(example = 'Молоко')

# class BaseFilm(BaseModel):
#     id: int = Field(example = 1)
#     name: str = Field(example = 'Название фильма')
#     rating: int = Field(example = 9)