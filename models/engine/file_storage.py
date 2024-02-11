#!/usr/bin/python3
"""filestorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent storage engine.

    Attributes:
        __file_path : name of  file to save to.
        __objects : dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return  dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets upo in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Sets __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Unsets the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for key, value in objdict.items():
                    cls_name = value["__class__"]
                    obj_id = value["id"]
                    del value["__class__"]
                    self.new(eval(cls_name)(**value))
        except FileNotFoundError:
            return

