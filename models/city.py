#!/usr/bin/env python3
"""city file that inherits from Base model
"""

from models.base_model import BaseModel


class City(BaseModel):
    """class city that will inherit from BaseModel
    """

    state_id = ""
    name = ""
