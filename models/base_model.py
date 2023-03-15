#!/usr/bin/python3
"""
This is the base class which defines all common attributes
/methods for other classes
"""
import uuid
import datetime
import models


class BaseModel():
    """This is the base class model that
    defines all attributes used by other classes"""

    def __init__(self, *args, **kwargs):
        """Defines the public instance attributes of id,
        created_at and updated_at
        """
        if (kwargs):
            for key in kwargs.keys():
                if key in ('created_at', 'updated_at'):
                    kwargs[key] = datetime.datetime.fromisoformat(kwargs[key])
                if key != '__class__':
                    setattr(self, key, kwargs[key])
                
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
       


    def __str__(self):
        """Prints the string representation of this base class"""
        return (f'[{__class__.__name__}] ({self.id}) {self.__dict__}')

    def save(self):
        """Updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        dictionary = self.__dict__
        dictionary['__class__'] = __class__.__name__
        dictionary['updated_at'] = self.updated_at.isoformat()
        dictionary['created_at'] = self.created_at.isoformat()
        return dictionary
