#!/usr/bin/python3
"""
takes in a URL and an email address
sends a POST request to the passed URL with the email parameter
And displays content

Args:
- URL
- Email
Return:
- content
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    load = {"email": argv[2]}
    r = requests.post(url, data=load)
    print(r.text)
