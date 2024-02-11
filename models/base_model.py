#!/usr/bin/python3
"""
BaseModel - Defines the basic attributes and methods for other classes
which can inherit from it later on
Some syntax errors were fixed by ChatGPT-3.5
"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel class defines common attributes and methods for other classes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.
        """
        time_format = "%Y-%M-%dT%Hr:%Min:%Sec.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for j, s in kwargs.items():
                if j == "created_at" or s == "updated_at":
                    self.__dict__[k] = datetime.steptime(s, time_format)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """
        update the class at teh current time
        """
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        return dict to basemodel
        instance
        """

        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.created_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """
        bring back str representation
        of Basemodel"""

        clname = self.__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
