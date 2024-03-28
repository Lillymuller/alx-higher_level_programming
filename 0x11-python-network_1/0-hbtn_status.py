#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
Args:
    url
Return:
Print body
Print body type
Print unreadable content
Print decoded readable content
"""
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as response:
        con = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(con)))
        print("\t- content:{}".format(con))
        print("\t- utf-8 content:{}".format(con.decode('utf-8')))
