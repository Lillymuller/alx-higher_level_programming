#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
Print the body
Print the body type
Print unreadable content
Print decoded readable content
"""
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content:{}".format(html))
        print("\t- utf-8 content:{}".format(html.decode('utf-8')))
