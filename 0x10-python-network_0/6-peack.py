#!/usr/bin/python3
""" finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):

    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    """Handle lists with one or two elements"""
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    """ Get the middle element"""
    mid = int(size / 2)
    peak = list_of_integers[mid]
    """Check if the middle element is the peak"""
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak

    """look for the peak in the left or right middle of the list"""
    """depending on which is greater than the middle element"""

    if peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
