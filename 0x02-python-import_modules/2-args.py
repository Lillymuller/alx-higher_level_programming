#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
   inputs = len(argv)
    if inputs > 1:
        count = 0
        if inputs > 2:
            print("{:d} arguments:".format(inputs - 1))
        else:
            print("{:d} argument:".format(inputs - 1))
        for arg in argv:
            count += 1
            if count != 1:
                print("{:d}: {}".format(count - 1, arg))
    else:
        print("0 arguments.")
