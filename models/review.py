#!/usr/bin/env python3
"""class review file that inherits from Basemodel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """class review that will be inheriting from baseModel
    """

    place_id = ""
    user_id = ""
    text = ""
