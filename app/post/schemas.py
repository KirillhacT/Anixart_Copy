from pydantic import BaseModel
from datetime import date
from typing import Optional, Literal
class SPost(BaseModel):
    id: int
    release_date: date
    name: str
    alternative_name: str
    type: Literal['ТВ-сериал', 'OVA', 'ONA', 'Фильм']
    status: Literal["Онгоинг", "Завершенный", "Анонс"]
    description: str
    series_count: int
    photo_id: Optional[int]
    franchise_id: Optional[int]
    rating: float

    class Config:
        orm_mode = True