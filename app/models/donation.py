from sqlalchemy import Column, ForeignKey, Integer, Text

from .abstract_model import Abstract


class Donation(Abstract):
    user_id = Column(Integer, ForeignKey("user.id"))
    comment = Column(Text)
