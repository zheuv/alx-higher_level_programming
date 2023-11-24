#!/usr/bin/python3

def printint(integer):
    try:
        if not isinstance(integer, int):
            raise TypeError

        print("{:d}".format(integer))
    except TypeError:
        return False
    else:
        return True
