#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0

    try:
        # Check if my_list is a list and x is an integer
        if not isinstance(my_list, list):
            raise TypeError("my_list should be a list")
        if not isinstance(x, int):
            raise TypeError("x should be an integer")

        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass  # Catch the IndexError and do nothing
    except TypeError as e:
        print(f"Error: {e}")

    print()  # Print a newline after the elements

    return count
