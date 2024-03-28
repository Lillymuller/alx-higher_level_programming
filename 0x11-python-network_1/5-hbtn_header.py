#!/usr/bin/python3
"""sends a request to the URL and displays X-Request-Id
in the response header
"""
import requests
from sys import argv


if __name__ == "__main__"
r = requests.get(argv[1])
res = r.headers.get('X-Request-Id')
print(res)
