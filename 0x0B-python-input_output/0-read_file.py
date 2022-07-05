#!/usr/bin/python3
"""
Module 0-read_file.py
"""


def read_file(filename=""):
    """ function that reads a text file """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
