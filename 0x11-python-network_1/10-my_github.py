#!/usr/bin/python3
"""
Uses GitHub API to show GitHub ID based on credentials
Args:
- url
- author name
Return:
- ID
"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/user"
    name = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get(url, auth=name)
    print(res.json().get("id"))
