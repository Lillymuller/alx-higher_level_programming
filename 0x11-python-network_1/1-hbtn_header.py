#!/usr/bin/python3
"""send a request to the URL and displays the value of the X-Request-Id"""
import urllib.request
from os import argv


if __name__ == "__main__":
    request = urllib.request.Request(argv[1])
    with urllib.request.urlopen(request) as response:
        """check if the header is there and print it out"""
        print(response.getheader['X-Request-Id'], None)
