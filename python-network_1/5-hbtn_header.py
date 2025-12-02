#!/usr/bin/python3
"""
Sends a request to a URL and displays the value of X-Request-Id
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    print(response.headers.get("X-Request-Id"))
