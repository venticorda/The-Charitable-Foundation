from sqlalchemy import Column, String, Text

from .abstract_model import Abstract
from app.services.constants import MAX_LEN_STRING


class CharityProject(Abstract):
    name = Column(String(MAX_LEN_STRING), unique=True, nullable=False)
    description = Column(Text, nullable=False)
