#!/usr/bin/python3
for i in range(0, 10):
    for n in range((i+1), 10):
        if (i is not 8) or (n is not 9):
            print("{}{}, ".format(i, n), end="")
        else:
            print("{}{}".format(i, n))
