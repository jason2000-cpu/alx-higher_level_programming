#!/usr/bin/python3
"""
This script takes in an argument and displays all values
in the 'states' table  where name matches the argument
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    # query = "SELECT * FROM states WHERE name = %s"
    cur.execute("SELECT * FROM states WHERE name = %s", (sys.argv[4],))
    states = cur.fetchall()

    for state in states:
        print(state)
