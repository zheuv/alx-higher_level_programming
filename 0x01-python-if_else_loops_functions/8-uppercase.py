#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        c = str[i]
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end='')
    print()

