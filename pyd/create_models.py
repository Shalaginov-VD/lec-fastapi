from pydantic import BaseModel, Field


class CreateProduct(BaseModel):
    name: str = Field(min_length = 3, max_length = 255, example = 'Молоко')

class CreateFilm(BaseModel):
    name: str = Field(min_length = 5, max_length = 255, example = 'Название фильма')
    rating: int = Field(gt = 0, example = 9)