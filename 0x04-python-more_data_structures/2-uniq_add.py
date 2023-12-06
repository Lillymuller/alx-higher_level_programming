#!/usr/bin/python3
def uniq_add(my_list=[]):
    Sum = 0
    for i in set(my_list):
        Sum += i
    return(Sum)

