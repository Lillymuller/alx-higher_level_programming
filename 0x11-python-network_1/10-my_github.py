#!/usr/bin/python3
"""
Uses GitHub API to show GitHub ID based on credentials
HTTPBasicAuth transmits username, password embedded directly in HTTP
Base64 is encoding used in HTTPBasicAuth, it should be used with HTTPS

Args:
- url
- author name
- token
Return:
- ID
"""
import requests
from sys import argv
from sys import exit
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    """checking argument count"""
    if len(argv) != 3:
        exit(f"Usage: script.py <username> <personal_access_token>")
    url = "https://api.github.com/user"
    name = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get(url, auth=name)

    if res.status_code == 200:
        data = res.json()
    else:
        print(f"Error: Request failed status code: {res.status_code}")
