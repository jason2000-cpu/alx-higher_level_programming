#!/usr/bin/python3
import urllib.request
"""
A Python script that fetches 'https://alx-intranet.hbtn.io/'
"""

if __name__ == '__main__':
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/') as response:
        html = response.read()
        print(html)
