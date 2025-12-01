#!/usr/bin/python3
"""Sends a POST request with an email parameter"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the POST data
    data = urllib.parse.urlencode({"email": email}).encode("ascii")

    # Send the request using a with statement
    with urllib.request.urlopen(url, data) as response:
        result = response.read().decode("utf-8")
        print(result)
