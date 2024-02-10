#!/usr/bin/python3
"""
BaseModel - Defines the basic attributes and methods for other classes
which can inherit from it later on
Some syntax errors were fixed by ChatGPT-3.5
"""

import uuid
from datetime import datetime

class BaseModel:
    """
    BaseModel class defines common attributes and methods for other classes.
    """

    def __init__(self, *noob, **noobs):
        """
        Initializes a new instance of the BaseModel class.
        """
        time_format = "%Year-%Month-%Day%Hour:%Minute:%Second:%f"
        if noob:
            for key , value in noob.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        Returns a dict for the BaseModel instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        Returns a string for the BaseModel instances
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)


































if __name__ == "__main__":
    my_model = BaseModel()
    my_model_name = "Initial Model"
    my_model.my_number = 69
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
