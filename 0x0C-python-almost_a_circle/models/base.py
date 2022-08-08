#!/usr/bin/python3
"""This module contains he Base class which would be the
'base' of other project classes
"""


import csv
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
        if id is not None:
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
        if list_dict is not None and len(list_dict) > 0:
            return json.dumps(list_dict)
        return ("[]")

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of
        list_objs to a file
        """
        filename = f"{cls.__name__}.json"
        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                new_l = [obj.to_dictionary() for obj in list_objs]
                new_d = cls.to_json_string(new_l)
                f.write(new_d)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string
        representation json_string
        """
        if json_string is None or len(json_string) < 1:
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
        if os.path.exists(filename) is False:
            return ([])
        else:
            with open(filename, "r", encoding="utf-8") as f:
                file_data = f.read()
                data_list = cls.from_json_string(file_data)
                return [cls.create(**item) for item in data_list]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes a CSV file """
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            if list_objs is None:
                writer.writerow([])
            else:
                if cls.__name__ == "Rectangle":
                    for obj in list_objs:
                        obj_l = [obj.id, obj.width, obj.height, obj.x, obj.y]
                        writer.writerow(obj_l)
                elif cls.__name__ == "Square":
                    for obj in list_objs:
                        obj_l = [obj.id, obj.size, obj.x, obj.y]
                        writer.writerow(obj_l)

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes a CSV file """
        filename = f"{cls.__name__}.csv"
        obj_list = []
        if os.path.exists(filename) is False:
            return ([])
        else:
            with open(filename, "r", encoding="utf-8") as f:
                csv_data = csv.reader(f)
                for data in csv_data:
                    if cls.__name__ == "Rectangle":
                        dictionary = {
                                "id": int(data[0]),
                                "width": int(data[1]),
                                "height": int(data[2]),
                                "x": int(data[3]),
                                "y": int(data[4])
                                }
                    elif cls.__name__ == "Square":
                        dictionary = {
                                "id": int(data[0]),
                                "size": int(data[1]),
                                "x": int(data[2]),
                                "y": int(data[3])}
                    obj = cls.create(**dictionary)
                    obj_list.append(obj)
        return (obj_list)
