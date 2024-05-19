#!/usr/bin/python3
""" module file for user class that inherits from baseModel """

from models.base_model import BaseModel


class User(BaseModel):
    """ class userfile inherits from the basemodel """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
