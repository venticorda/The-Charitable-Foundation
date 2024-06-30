from datetime import datetime

from sqlalchemy import Column, Integer, Boolean, DateTime

from app.core.db import Base
from app.services.constants import (DEFAULT_INVESTED_AMOUNT,
                                    DEFAULT_FULLY_INVESTED)


class Abstract(Base):
    __abstract__ = True

    full_amount = Column(Integer, nullable=False)
    invested_amount = Column(Integer, default=DEFAULT_INVESTED_AMOUNT)
    fully_invested = Column(Boolean, default=DEFAULT_FULLY_INVESTED)
    create_date = Column(DateTime, default=datetime.now)
    close_date = Column(DateTime)
