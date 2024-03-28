#!/usr/bin/python3
"""Uses GitHub API to show GitHub ID based on  credentials"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/user"
    name = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get(url, auth=name)
    print(f"ID: {res.json().get("id")}")
