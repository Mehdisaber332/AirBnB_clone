#!/usr/bin/python3
"""models to import"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os


class FileStorage:
    """serializes/deserializes instances to a JSON file"""
    __file_path = "str.json"
    __objects = {}
    classes = {"BaseModel": BaseModel,
               "User": User,
               "Place": Place,
               "State": State,
               "City": City,
               "Amenity": Amenity,
               "Review": Review
               }

    def all(self):
        """returns objects"""
        return self.__objects

    def new(self, obj):
        """adds new object"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        _data = dict(self.__objects)
        for key, obj in _data.items():
            _data[key] = obj.to_dict()
        with open(self.__file_path, "w") as file:
            json.dump(_data, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        _data = self.__objects
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path,
                          mode="r", encoding="utf-8") as f:
                    json_dict = json.load(f)
                    for key, value in json_dict.items():
                        if "BaseModel" in key:
                            _data[key] = BaseModel(**value)
                        elif "User" in key:
                            _data[key] = User(**value)
                        elif "State" in key:
                            _data[key] = State(**value)
                        elif "City" in key:
                            _data[key] = City(**value)
                        elif "Amenity" in key:
                            _data[key] = Amenity(**value)
                        elif "Place" in key:
                            _data[key] = Place(**value)
                        elif "Review" in key:
                            _data[key] = Review(**value)
            except FileExistsError:
                pass
