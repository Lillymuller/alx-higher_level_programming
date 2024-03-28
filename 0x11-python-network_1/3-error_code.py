#!/usr/bin/python3
"""
manage urllib.error.HTTPError exceptions
And prints the error code
"""
import urllib.request
import urllib.error
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = urllib.request.Request(argv[1])

    try:
        with urllib.request.urlopen(req) as response:
            res = response.read().decode('utf-8')
            print(res)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
