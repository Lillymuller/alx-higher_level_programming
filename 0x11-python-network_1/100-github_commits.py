#!/usr/bin/python3
"""
Takes 2 arguments in order to solve this challenge.
Args:
- repository name
- owner name
- 
"""
import requests
from sys import argv


if __name__ == "__main__":
    base_url = "https://api.github.com/repos/{}/{}/commits/latest"
    owner = argv[1]
    repo = argv[2]

    url = base_url.format(owner, repo)
    try:
        r = requests.get(url)
        r.raise_for_status()

        data = response.json()
        commit_message = data["commit"]["message"]
        print(f"Commit message for {owner}/{repo}: {commit_message}")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError:
        print(f"Error: Invalid data format or missing key in response.")
    except Exception as e:
        print(f"Unexpected error: {e}")
