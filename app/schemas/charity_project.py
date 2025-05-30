from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, PositiveInt

from app.services.constants import (
    DEFAULT_FULLY_INVESTED,
    DEFAULT_INVESTED_AMOUNT,
    MAX_LEN_STRING,
    MIN_LEN_STRING,
)


class CharityProjectBase(BaseModel):
    name: Optional[str] = Field(None, max_length=MAX_LEN_STRING)
    description: Optional[str] = Field(None)
    full_amount: Optional[PositiveInt] = Field(None)

    class Config:
        extra = Extra.forbid
        min_anystr_length = MIN_LEN_STRING


class CharityProjectCreate(BaseModel):
    name: str = Field(max_length=MAX_LEN_STRING)
    description: str
    full_amount: PositiveInt

    class Config:
        min_anystr_length = MIN_LEN_STRING


class CharityProjectDB(CharityProjectCreate):
    id: int
    invested_amount: int = Field(DEFAULT_INVESTED_AMOUNT)
    fully_invested: bool = Field(DEFAULT_FULLY_INVESTED)
    create_date: datetime
    close_date: Optional[datetime]

    class Config:
        orm_mode = True


class CharityProjectUpdate(CharityProjectBase):
    pass
