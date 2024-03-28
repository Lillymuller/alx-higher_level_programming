#!/usr/bin/python3
"""
sends a POST request to http://0.0.0.0:5000/search_user with parameter
Args:
q
argv
Return:
Not a valid JSON if the JSON is invalid
No result if the JSON is empty
"""
import requests
from sys import argv

if __name__ == "__main__":
    if  len(argv) < 2:
        letter = argv[1]
    else:
        letter=""

send = {"q": letter}
res = requests.post("http://0.0.0.0:5000/search_user", data=send)
try:
    data = responce.json()
    if not data:
        print("No result")
    else:
        print(f"[{data.get('id')}] {data.get('name')}")
except json.JSONDecodeError:
    print("Not a Vaild Json")
