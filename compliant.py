import uuid
from datetime import datetime
import json
import os

class BaseModel:
    objects = {}

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', str(uuid.uuid4()))
        self.created_at = kwargs.get('created_at', datetime.now().isoformat())
        self.updated_at = kwargs.get('updated_at', self.created_at)
        self.__class__.objects[self.id] = self

    def save(self):
        self.updated_at = datetime.now().isoformat()
        with open('storage.json', 'w') as file:
            json.dump(self.to_dict(), file)

    def to_dict(self):
        return {
                'id': self.id,
                'created_at': self.created

