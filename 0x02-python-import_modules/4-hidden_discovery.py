#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    for string in dir(hidden_4):
        if string[0:2] =! '__':
            print(string)
