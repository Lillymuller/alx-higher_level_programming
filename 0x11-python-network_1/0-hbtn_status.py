#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
Prints the body
prints the body type
prints unreadable content
prints decoded readable content
"""
import urllib.request


if __name__ == "__main__":

    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        html = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf-8 content: {body.decode('utf-8')}") 
