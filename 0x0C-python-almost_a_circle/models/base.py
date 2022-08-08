#!/usr/bin/python3
"""This module contains he Base class which would be the
'base' of other project classes
"""


import json
import os.path


class Base:
    """This class will be the “base” of all other classes
    in this project.
    The goal of it is to manage id attribute in all your
    future classes and to avoid duplicating the same
    code (by extension, same bugs)
    """
    __nb_objects = 0
    def __init__(self, id=None):
        """Initializer function"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base. __nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of
        list_dictionaries
        """
        list_dict = list_dictionaries
        if list_dict != None and len(list_dict) > 0:
            return json.dumps(list_dict)
        return ("[]")

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of
        list_objs to a file
        """
        filename = f"{cls.__name__}.json"
        with open(filename, "w", encoding = "utf-8") as f:
            if list_objs == None:
                f.write([])        
            else:
                new_l = [obj.to_dictionary() for obj in list_objs]
                new_d = cls.to_json_string(new_l)
                with open(filename, "w", encoding = "utf-8") as f:
                    f.write(new_d)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string
        representation json_string
        """
        if json_string == None or len(json_string) < 1:
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already
        set
        """
        inst = cls(1, 2, 3)
        inst.update(**dictionary)
        return (inst)

    @classmethod
    def load_from_file(cls):
        """Returns the list of instances"""
        filename = f"{cls.__name__}.json"
        if os.path.exists(filename) == False:
            return ([])
        else:
            with open(filename, "r", encoding="utf-8") as f:
                file_data = f.read()
                data_list = cls.from_json_string(file_data)
                return [cls.create(**item) for item in data_list]
