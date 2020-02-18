#!/usr/bin/python3
""" This module contains class City
"""


import models
from models.base_model import BaseModel


class City(BaseModel):
    """
            Class City that inherits from BaseModel
    """
    state_id = ""
    name = ""
