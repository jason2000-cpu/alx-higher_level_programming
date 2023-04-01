#!/usr/bin/python3
import urllib.request
"""
A Python script that fetches 'https://alx-intranet.hbtn.io/'
"""

with urllib.request.urlopen('https://alx-intranet.hbtn.io/') as response:
    html = response.read()
    print(html)
