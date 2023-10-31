#!/usr/bin/python3

def remove_char_at(string, n):
    # Check if n is negative and adjust it to a positive index
    if n < 0:
        return string

    # Initialize an empty string to store the modified result
    result = ""

    # Iterate through the characters in the string
    for i in range(len(string)):
        # Skip the character at index n
        if i == n:
            continue
        else:
            # Append the character to the result string
            result += string[i]

    return result
