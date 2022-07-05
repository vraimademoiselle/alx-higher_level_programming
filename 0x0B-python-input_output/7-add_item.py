#!/usr/bin/python3
"""
Module 7-add_item.py
"""

import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"

try:
    content = load_from_json_file(filename)
except FileNotFoundError:
    content = []
content.extend(sys.argv[1:])
save_to_json_file(content, filename)
