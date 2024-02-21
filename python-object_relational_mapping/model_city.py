#!/usr/bin/python3

"""
Define City class -> Base,
using SQLAlchemy
"""

from sqlalchemy import Column, String, Integer, CHAR, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    __tablename__ = "cities"
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(128), nullable=False)
    state_id = Column('state_id', ForeignKey('states.id'), Integer, nullable=False, )
