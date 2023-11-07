#!/usr/bin/python3
"""models to import"""

import json
from models.base_model import BaseModel
import os


class FileStorage:
    """serializes/deserializes instances to a JSON file"""
    __file_path = "str.json"
    __objects = {}

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
            except FileExistsError:
                pass
