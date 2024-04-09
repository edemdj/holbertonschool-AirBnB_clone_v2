#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='delete')

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Returns the list of City instances"""
            cities_instances = []

            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    cities_instances.append(city)
            return cities_instances
        
    if models.storage == "DBStorage":
        @property
        def cities(self):
            """add a guetter methode to return city"""
            from models import storage
            return [city for city in storage.all(City).values() if city.state_id == self.id]
