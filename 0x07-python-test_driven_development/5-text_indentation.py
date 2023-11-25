#!/usr/bin/python3
"""
5-text_indentation module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """Splits a text into lines along "?", ":", "." followed by 2 new lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    length = len(text) -1

    while length >= 0 and text[length] == ' ':
        length = length - 1


    start_of_the_line = True

    for char in range(length + 1):
        if text[char] == ' ' and start_of_the_line:
            continue
        else:
            print(text[char], end='')
            start_of_the_line = False
            if text[char] in [".", "?", ":"]:
                print()
                print()
                start_of_the_line = True

