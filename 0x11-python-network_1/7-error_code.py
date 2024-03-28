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
        response.raise_for_status()
        print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Error code: {responce.status_code}" if response
                else "Error: Failed to connect")
    except Exception as e:
        print(f"Unexpected error: {e}")
