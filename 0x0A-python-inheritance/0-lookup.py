#!/usr/bin/python3
"""
Module 0-lookup.py
contains lookup funtion that returns a
list of attr and methods.
"""


def lookup(obj):
    """
    Returns a list object
    """
    return dir(obj)
