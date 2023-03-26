#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    '''A class that creates a user class which inherits from basemodel'''
    text = ''
    place_id = ''
    user_id = ''
