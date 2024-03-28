#!/usr/bin/python3
"""
If the HTTP status code is greater than or equal to 400, print: Error code
followed by the value of the HTTP status code
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    res = requests.get(url)
    if res.status_code >= 400:
        print(f"Error: {res.status_code}")
    else:
        print(res.text)

