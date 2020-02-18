#!/usr/bin/python3
""" This module contains class Review
"""


import models
from models.base_model import BaseModel


class Review(BaseModel):
    """
            class Review that inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
