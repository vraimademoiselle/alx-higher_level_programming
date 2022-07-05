#!/usr/bin/python3
"""
Module 10-student.py
"""


class Student():
    """
    Represent a student
    """

    def __init__(self, first_name, last_name, age):
        """ Initialize a new Student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student
        """
        if attrs is None:
            return self.__dict__
        else:
            dic = {}
            for att in attrs:
                if att in self.__dict__.keys():
                    dic[att] = self.__dict__[att]
            return dic
