#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends POST request
 to the passed URL with the email as a parameter and disaplays
 the body of the response(decoded in utf-8)
"""


import sys
import urllib.request
import urllib.parse

values = {'email': sys.argv[2]}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')  # data should be bytes
req = urllib.request.Request(sys.argv[1], data)
with urllib.request.urlopen(req) as response:
    the_page = response.read()
    print(the_page)
