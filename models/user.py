#!/usr/bin/python3
"""a user class will be defined here"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    the above mentioned class
    Attributes  : email: string - empty string
password: string - empty string
first_name: string - empty string
last_name: string - empty string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
