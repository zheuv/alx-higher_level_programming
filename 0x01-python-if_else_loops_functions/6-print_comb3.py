#!/usr/bin/python3
for i in range(100):
    if i < int(str(i % 10) + str(i // 10)):
        code = "{:02d}".format(i)
        if i != 89:
            print(code, end=', ')
        else:
            print(code)
