#!/usr/bin/python3

def printint(integer):
    try:
        print("{:d}".format(integer))

    except ValueError:
        return False
    else:
        print()
        return True

printint(5)
