#!/usr/bin/env python3
"""This module will serialize and deserialize objects to
and from json file
"""

import json


class FileStorage:
    """This module will define a class to serialize and
    deserialize json
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This module will return  the dictionary __objects
        """

        return FileStorage.__objects

    def new(self, obj):
        """This module sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """This module serializes __objects to the JSON file (path: __file_path)
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
             my_dict = {}
             for key, value in FileStorage.__objects.items():
                 my_dict[key] = value.to_dict()
            json.dump(my_dict, f)

    def reload(self):
        """This module deserializes from a json file
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        class_dict = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
                }
        obj = FileStorage.__objects
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                json_data = json.load(f)
                for key, value in json_data.items():
                    obj[key] = class_dict[value["__class__"]](**value)
        except FileNotFoundError:
            pass
