#!/usr/bin/python3
""" the implementation of the State class """

import SQLAlchemy
from SQLAlchemy import Column, String, Integer

Base = SQLAlchemy.ext.declarative_base()

class State(Base):
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
