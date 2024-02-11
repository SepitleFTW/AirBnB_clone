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
    """Represeage engine.

    Attributes:
        __objects : tionay  objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Retur_objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets upo in __o <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Sets __objects  """
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Unsets """
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

