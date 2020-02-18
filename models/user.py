#!/usr/bin/python3
""" This module contains BaseModel class
"""


import models
from models.base_model import BaseModel


class User(BaseModel):
    """ User class define user information
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
