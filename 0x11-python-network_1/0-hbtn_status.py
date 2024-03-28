#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
Args:
    url
Return:
- Print body
- Print body type
- Print unreadable content
- Print decoded readable content
"""
import urllib.request


if __name__ == "__main__":
    r = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(r) as response:
        con = response.read()
        print("Body response:")
        print("\t- type: " + str(type(con)))
        print("\t- content: " + str(con))
        print("\t- utf8 content: " + str(con.decode('utf-8')))
