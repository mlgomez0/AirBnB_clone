#!/usr/bin/python3
""" This module contains class FileStorage
"""


import json
import os
class FileStorage():
    """ Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = 'file.json'
    __objects = {}

    def __init__(self):
        """ Constructor of class FileStorage
        """
        pass

    def all(self):
 |       """ returns the dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """  sets in __objects the obj with key <obj class name>.id
        """
        class_id = obj.__class__.__name__ 
        class_id = class_id + '.' + obj.id
        __objects[class_id] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)
        """
        if not os.path.exists(FileStorage.__file_path):
            str_json = json.dumps(FileStorage.__objects)
        else:
            with open(FileStorage.__file_path, "r", encoding='utf-8') as my_file:
                str_json = my_file.read()
            my_obj = json.loads(str_json)
            my_obj[my_obj.__class__.__name__ + '.' + my_obj.id] = self.__dict__)
            str_json = json.dumps(my_obj)
        with open(FileStorage.__file_path, "w", encoding='utf-8') as my_file:
            my_file.write(str_json)

    def reload(self):
        """ deserializes the JSON file to __objects (only if the JSON file 
            (__file_path) exists ; otherwise, do nothing. 
            If the file doesn’t exist, no exception should be raised)
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as my_file:
                str_read = my_file.read()
            my_obj = json.loads

                

