#!/usr/bin/python3
import urllib.request
"""
A Python script that fetches 'https://alx-intranet.hbtn.io/'
"""

req = urllib.request.Request('https://alx-intranet.hbtn.io/')
with urllib.request.urlopen(req) as response:
    html = response.read()
