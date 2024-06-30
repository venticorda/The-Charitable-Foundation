from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, PositiveInt, validator

from app.services.constants import DEFAULT_INVESTED_AMOUNT


class DonationBase(BaseModel):
    full_amount: PositiveInt
    comment: Optional[str]


class DonationCreate(DonationBase):
    id: int
    create_date: datetime

    @validator("create_date", pre=True, always=True)
    def set_create_date(cls, value):
        return value or datetime.now

    class Config:
        orm_mode = True


class DonationDB(DonationCreate):
    id: int
    create_date: datetime
    user_id: int
    invested_amount: int = Field(DEFAULT_INVESTED_AMOUNT)
    fully_invested: bool
    close_date: Optional[datetime]
