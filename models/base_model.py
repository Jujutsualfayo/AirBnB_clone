#!/usr/bin/env python3
"""This file will illustrate all the common attributes
for other classes.
"""
import uuid
from datetime import datetime, time, date
from models import storage


class BaseModel:
    """This is a base class for all the 
    models such as methods and created_at
    """

    def __init__(self, *args, **kwargs):
        """creates the class attributes for a Base instance.
        """

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        value = datetime.\
                                strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)

    def __str__(self):
        """It will return  a string representation of the class
        """

        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """updates the updated_at attr
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """It will return a dict representation of the instance
        """

        my_dict = self.__dict__.copy()
        my_dict.update({
            "__class__": self.__class__.__name__,
            "updated_at": self.updated_at.isoformat(),
            "created_at": self.created_at.isoformat()
            })
        return my_dict
