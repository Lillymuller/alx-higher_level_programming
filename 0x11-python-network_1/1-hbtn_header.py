#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""
import urllib.request
from os import argv


if __name__ == "__main__":
    """Fetches fron the given URL the X-Request-ID header"""
    request = urllib.request.Request(argv[1])
    with urllib.request.urlopen(request) as response:
        """check if the header is there and print it out"""
        if 'X-Request-Id' in response.headers:
            print(response.headers['X-Request-Id'])
