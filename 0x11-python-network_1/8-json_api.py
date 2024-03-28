#!/usr/bin/python3
"""
sends a POST request to http://0.0.0.0:5000/search_user with parameter
Args:
    q: query
    argv: arguments
Return:
    Not a valid JSON if the JSON is invalid
    No result if the JSON is empty
"""
import requests
from sys import argv


if __name__ == "__main__":
    """Check for arguments and set the q param"""
    if  len(argv) > 1:
        q = argv[1]
    else:
        q=""

"""Build the URL with query"""
url = f"http://0.0.0.0:5000/search_user?=q{q}"

"""Send a Post Request"""
try:
    response = requests.post(url)
    response.raise_for_status()
except requests.rxceptions.RequestException as e:
    print(f"Error sending request: {e}")

"""checking for valid Json response"""
try:
    data = responce.json()
except json.JSONDecodeError:
    print("Not a Vaild Json")

"""check for empty responses"""
if not data:
    print("No result")

for user in data:
    print(f"[{user['id']}] {user['name']}")
