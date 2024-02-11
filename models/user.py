#!/usr/bin/python3
"""a user class will be defined here"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    the above mentioned class
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
