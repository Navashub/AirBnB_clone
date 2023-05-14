#!/usr/bin/python3
"""base_model.py that contains BaseModel class module."""


from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """class BaseModel that defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """
        Initializes  objects of the BaseModel class.

        args:
            id (string): unique identity of the instance
            created_at (datetime): date/time the instance was created
            updated_at (datetime): date/time the instance was updated
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == "updated_at":
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
            self.id = kwargs.get('id', str(uuid4()))
            self.created_at = kwargs.get('created_at', datetime.now())
            self.updated_at = kwargs.get('updated_at', datetime.now())
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """This method returns a string represetation of any of the class Base instance."""
        clName = type(self).__name__
        return "[{}] ({}) {}".format(clName, self.id, self.__dict__)

    def save(self):
        """Updates the current time to updated_at"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """This returns a dict. as rep of any BaseModel instance."""
        dict_repr = self.__dict__.copy()
        dict_repr['__class__'] = type(self).__name__
        dict_repr['created_at'] = self.created_at.isoformat()
        dict_repr['updated_at'] = self.updated_at.isoformat()
        return dict_repr
