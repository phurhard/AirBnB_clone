#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    '''A class that creates a user class which inherits from basemodel'''
    email = ''
    password = ''
    first_name = ''
    last_name = ''
