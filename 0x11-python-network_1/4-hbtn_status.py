#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests


if __name__ == "__main__":
    """Fetch status form the given URL and display it's content"""
    r = requests.get("https://alx-intranet.hbtn.io/status")
        """printing the body content"""
        print("Body response:")
        """lets check the body type in bytes"""
        print(f"\t- type: {type(r.text)}")
        """the raw content unreadable for text data"""
        print(f"\t- content: {r.text}")
