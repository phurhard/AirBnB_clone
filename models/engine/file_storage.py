#!/usr/bin/python3
'''This class creates a storage for storing our objects created from previous running of the program and restores all objects created before'''
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.state import State


class FileStorage():
    '''This is a file storage that stores the ojects created'''
    def __init__(self, *args, **kwargs):
        '''Initializations of required attributes'''
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        '''Returns all the dictionary representation present in __objects'''
        return self.__objects

    def new(self, obj):
        '''Creates a new instance of storage and sets in __objects the obj class name and id'''
        self.__objects[obj.__class__.__name__+'.'+obj.id] = obj

    def save(self):
        '''Serializes __objects to JSON and stores it in the file: file_path'''
        json_dictionary = {}
        for k,v in self.__objects.items():
            json_dictionary[k] = v.to_dict()
        with open(self.__file_path, 'w') as f:
            f.write(json.dumps(json_dictionary))

    def reload(self):
        '''Deserializes the JSO files into __objects (Only if the file exists, otherwise do nothing)'''
        try:
            with open(self.__file_path, 'r') as f:
                base_file = json.loads(f.read())
                for k,v in base_file.items():
                    self.__objects[k] = eval(v['__class__'])(**v)
        except Exception as e:
            pass

