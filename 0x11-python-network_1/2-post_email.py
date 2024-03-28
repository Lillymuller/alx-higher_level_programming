#!/usr/bin/python3
"""Sends Post request to the given URL with provided Email
Args:
url: the url to send the request to
email: the email address to send on the request body

Returns: the decoded content from the server
"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    values = {'email': argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    request = urllib.request.Request(url, data)

    with urllib.request.urlopen(request) as response:
        response_content = response.read().decode('utf-8')
        print(response_content)
