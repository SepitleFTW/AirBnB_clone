#!/usr/bin/python3
"""
this is the review class module
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """
    review class for all the reviews
    place is place
    user_id is the user id
    text is the text of teh review
    """

    place_id = ""
    user_id = ""
    text = ""
