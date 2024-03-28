#!/usr/bin/python3
"""
If the HTTP status code is greater than or equal to 400, print: Error code
followed by the value of the HTTP status code
"""
import requests
from sys import argv


if __name__ == "__main__":
    res = requests.get(argv[1])
    if res.status_code >= 400:
        print("Error: {}".format(res.status_code))
    else:
        print(res.text)

