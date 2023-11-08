#!/usr/bin/python3

def roman_to_int(roman_string):
    if isinstance(roman_string, str):
        
        my_dict = {'I':1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        
        for i in range(0,len(roman_string)):
            if i != len(roman_string) - 1:
                if my_dict[roman_string[i]] < my_dict[roman_string[i+1]]:
                    result = result - my_dict[roman_string[i]]
                else:
                    result = result + my_dict[roman_string[i]]
            else:
                result = result + my_dict[roman_string[i]]
        return result
    return 0
