#!/usr/bin/python3
""" This module contains BaseModel class
"""
import uuid
import json
import datetime

class BaseModel():
    """ BaseModel that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """ Constructor of class BaseModel
        """
        if kwargs:
            for k, v in kwargs.items():
                if k is not '__class__':
                    if k is 'created_at' or k is 'updated_at':
                        v = datetime.datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, k, v)
        else:
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
        a_dict['__class__'] = self.__class__.__name__
        a_dict['created_at'] = a_dict['created_at'].isoformat(sep='T')
        a_dict['updated_at'] = a_dict['updated_at'].isoformat(sep='T')
        return a_dict




