#!/usr/bin/python3
"""This function returns a list of attributes and methods of an object
"""

'''
File_Name: 0-lookup.py
Project Title: 0x0A-python-inheritance
'''


def lookup(obj):
    """
    # Write a function that returns the list of available attributes and....
    # .....methods of an object:
    # VARIABLE(" "):
    # LookUp(obj): Lookup
    # Return: a 'list' object.
    """
    """ This function takes an object as a parameter and returns the list...
    of attributes and methods using the 'dir()' function..."""
    return dir(obj)
