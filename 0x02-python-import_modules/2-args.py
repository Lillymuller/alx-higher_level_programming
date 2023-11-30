#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    inputs = argv[1:]
    size = len(inputs)
    print("{:d} {:s}{:s}".
          format(size,
                 "arguments" if (size) is not 1 else "argument",
                 "." if (size) is 0 else ":"))
    for count, args in enumerate(inputs):
        print("{:d}: {:s}".format(count + 1, args)
