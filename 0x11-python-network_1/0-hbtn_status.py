#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
    """Fetch status form the given URL and display it's content"""
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        html = response.read()
        """printing the body content"""
        print("Body responce:")
        """lets check the body type in bytes"""
        print(f"\t- type: {type(body)}")
        """the raw content unreadable for text data"""
        print(f"\t- content: {body}")
        """the readable decoded content using UTF-8 encoding"""
        print(f"\t- utf-8 content: {body.decode('utf-8')}") 
