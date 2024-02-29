#!/usr/bin/python3
""" the function in this module returns the peak in an unsorted list """

def find_peak(list):
    """this function finds a peak using biary search"""
    if list:
        begin = 0
        end = len(list) - 1

        while begin < end:
            mid = (begin + end) // 2
            if list[mid] > list[mid + 1]:
                end = mid
            else: 
                begin = mid + 1
        return list[begin]
