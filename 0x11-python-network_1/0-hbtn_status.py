#!/usr/bin/python3
import urllib.request
"""
A Python script that fetches 'https://alx-intranet.hbtn.io/'
"""

if __name__ == '__main__':
    """
    Code to fetch the url
    """
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/') as response:
        html = response.read()

    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)
    print("\t- utf8 content:", html.decode('utf-8'))
