#!/usr/bin/python3

"""
Define State class and create instance of Base,
using SQLAlchemy
"""

from sqlalchemy import Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State -> Base : Contains the definition of the State database

    Args:
        Base (class): declarative_base()
    """
    __tablename__ = "states"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String(128), nullable=False)
