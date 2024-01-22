#!/usr/bin/python3
"""
The module adds all arguments to a list, then saves that list to a file
"""
import sys


save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":

    try:
        arg_list = load_from_json("add.json")
    except FileNotFoundError:
        arg_list = []
    
    for arg in sys.argv[1:]:
        arg_list.append(arg)
    
    save_to_json(arg_list, "add.json")
