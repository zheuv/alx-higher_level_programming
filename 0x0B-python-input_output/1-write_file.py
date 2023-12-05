#!/usr/bin/pyhton3
"""contains the function write_file"""

def write_file(filename="", text=""):
    """ writes text to filename and returns the number of characters written"""
    with open(filename, 'w', encoding = "utf-8") as f:
        return f.write(text)
