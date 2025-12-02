#!/usr/bin/python3
"""
Uses GitHub API with Basic Authentication to display user id.
"""

import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]  # personal access token

    url = "https://api.github.com/user"

    response = requests.get(url, auth=(username, token))
    data = response.json()

    print(data.get("id"))
