#!/usr/bin/python3
""" Python file similar to model_state.py named model_city.py
    that contains the class definition of a City
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


class City (Base):
    """ Defines the city table """
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,
            ForeignKey("states.id"),
            nullable=False)
