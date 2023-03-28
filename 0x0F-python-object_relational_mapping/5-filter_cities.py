#!/usr/bin/python3
"""
This script takes in the name of a state as an
argument  and lists all 'cities' of that state
using the database 'hbtn_0e_4_usa'
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost', user=sys.argv[1],
        passwd=sys.argv[2], db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute(
        "SELECT name FROM cities\
        WHERE state_id = (SELECT id FROM states WHERE name = %s)",
        (sys.argv[4],))
    cities = cur.fetchall()

    print(", ".join([city[0] for city in cities]))
