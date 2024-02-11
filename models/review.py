#!/usr/bin/python3
""" review class definition"""
from models.base_model import BaseModle


class Review(BaseModel):
    """
    above mentioned class
    """

    place_id = ""
    user_id = ""
    text = ""
