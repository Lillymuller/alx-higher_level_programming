#!/usr/bin/python3
"""
If the HTTP status code is greater than or equal to 400 print Error code
Args:
    argv
Return:
    status code
"""
import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) < 2:
        print("Error: Please provide URL")

    url = argv[1]
    try:
        response = requests.get(url)
         if response.status_code >= 400:
             response.raise_for_status()
        print(response.text)
    except requests.exceptions.RequestException as e:
        err = responce.status_code
        print(f"Error code: {err if err else 'Failed to connect'}")
    except Exception as e:
        print(f"Unexpected error: {e}")
