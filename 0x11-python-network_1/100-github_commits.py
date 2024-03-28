#!/usr/bin/python3
"""
Takes 2 arguments in order to solve this challenge.
Args:
- repository name
- owner name
Return:
- latest 10 commits
"""
import requests
from sys import argv


if __name__ == "__main__":
    base_url = "https://api.github.com/repos/{}/{}/commits".format(argv[1], argv[2])

    try:
        r = requests.get(url)
        r.raise_for_status()

        data = response.json()
        for com in data:
            print(commit.get('sha'), end=': ')
            print(commit.get('commit', {}).get('author', {}).
                    get('name', '(unknown)'))
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError:
        print(f"Error: Invalid data format or missing key in response.")
    except Exception as e:
        print(f"Unexpected error: {e}")
