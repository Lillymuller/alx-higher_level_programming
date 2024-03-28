#!/usr/bin/python3
"""
If the HTTP status code is greater than or equal to 400 print Error code
Args:
    argv
Return:
    status code
"""
import requests
from sys import argv


if __name__ == "__main__":
    r = requests.get(argv[1])
    if r.status_code >= 400:
        print(f"Error: {r.status_code}")
    else:
        print(r.text)
