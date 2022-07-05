#!/usr/bin/python3
"""
Module 11-student.py
"""


class Student():
    """ Defines a student """

    def __init__(self, first_name, last_name, age):
        """ initializes attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns dictionary description with simple data structure
        """
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    dic[att] = self.__dict__[att]
            return dic

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student.
        """
        for k, v in json.items():
            setattr(self, k, v)
