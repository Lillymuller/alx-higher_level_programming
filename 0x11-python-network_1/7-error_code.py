#!/usr/bin/python3
"""
If the HTTP status code is greater than or equal to 400, print: Error code
followed by the value of the HTTP status code
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    """check if the status code is greater or equal to 400"""
    if r.status_code >= 400
    print(f"Error: {r.status_code}")
else:
    print(r.text)

