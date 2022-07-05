#!/usr/bin/python3
"""
Module 9-student.py
"""


class Student():
    """ defines a student """

    def __init__(self, first_name, last_name, age):
        """ initialization """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation of the Student."""
        return self.__dict__
