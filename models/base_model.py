#!/usr/bin/python3
""" This module contains BaseModel class
"""
import uuid
import json
import datetime

class BaseModel():
    """ BaseModel that defines all common attributes/methods for other classes
    """

    def __init__(self):
        """ Constructor of class BaseModel
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        
    def __str__(self):
        """ Overrides the str magic method
        """
        mge = "[BaseModel] ({}) {}"
        return mge.format(self.id, self.__dict__)

    def save(self):
        """ Updates the public instance attribute updated_at with the current datetime
        """
        updated_at = datetime.datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__ of the instance
        """
        a_dict = self.__dict__
        a_dict.update(__class__ = 'BaseModel')
        a_dict['created_at'] = a_dict['created_at'].isoformat(sep='T')
        a_dict['updated_at'] = a_dict['updated_at'].isoformat(sep='T')
        return a_dict



    
