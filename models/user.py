#!/usr/bin/python3
"""
user class' module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    user class for all the users
    and handles all their information
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
