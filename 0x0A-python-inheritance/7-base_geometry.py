#!/usr/bin/python3
"""
Module 7-base_geometry
Contains BaseGeometry
"""


class BaseGeometry:
    """
    Methods: area(self)
    """
    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates input Arguments
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer\n".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0\n".format(name))
