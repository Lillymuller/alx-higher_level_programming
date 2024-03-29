#!/usr/bin/python3
"""
Sends a POST request to http://0.0.0.0:5000/search_user with parameter.
Args:
- argv
Return:
- Print 'Not a valid JSON' if the JSON is invalid
- Print 'No result' if the JSON is empty
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) == 1:
        l = ""
    else:
        l = argv[1]
    send = {"q": l}
    res = requests.post("http://0.0.0.0:5000/search_user", data=send)
    try:
        data = res.json()
        if not data:
            print("No result")
        else:
            print(f"[{data.get('id')}] {data.get('name')}")
    except json.JSONDecodeError:
        print("Not a Vaild Json")
