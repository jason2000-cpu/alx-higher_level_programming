#!/usr/bin/python3
import sys
import urllib.request
"""
A Python script that takes in a URL, sends a request to the URL
and displays the value of the 'X-Request-Id' variable
"""

with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers['X-Request-Id'])
