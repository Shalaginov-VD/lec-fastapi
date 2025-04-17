from pydantic import BaseModel, Field

class BaseCategory(BaseModel):
    id: int = Field(example = 1)
    name: str = Field(example = 'Еда')

class BaseProduct(BaseModel):
    id: int = Field(example = 1)
    name: str = Field(example = 'Молоко')

class BaseFilm(BaseModel):
    id: int = Field(example = 1)
    name: str = Field(example = 'Название фильма')
    rating: int = Field(example = 9)