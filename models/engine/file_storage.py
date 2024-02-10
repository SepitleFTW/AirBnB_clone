#!/usr/bin/python3
"""
module for reading data and 'unreading' it
"""

import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    a class wwhere files will be stored in JSON
    """

    __file_path = "file.json"

    __object = {}

    def initialize(self, obj):
        """
        this will be added to basemodel constructor
        to be stored when called/passed

        """
        obj_cls_name = obj.__class__.__name__
        key = "{}.{}".format(obj_cls_name, obj.id)

        FileStorage.__object[key] = obj

    def everything(self):
        """
        I got this code ffrom CHATGPT3.5 lmao
        I was so confused
        """
        return FileStorage.__object

    def save(self):
        """
        serialise obj dict into json format
        basically to save into JSON
        """
        all_objs = FileStorage.__objects
        obj_dict = {}

        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj], to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        convert JSON file to python object
        """
        if os.path.isfile(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as file:
                try:
                    obj_dict = json.load(file)

                    for key, value in obj_dict.items():
                        class_name, obj_id = key.split(".")

                        cls = eval(class_name)
                        instance = cls(**value)

                        FileStorage.__objects[key] = instance
                except Exception:
                    pass
