#!/usr/bin/python3

"""
Display all cities from database,
safe from SQL injections, using MySQLdb
"""

import MySQLdb
import sys

if __name__ == "__main__":

    usr = sys.argv[1]
    pw = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host='localhost', user=usr, passwd=pw, db=database)
    cursor = db.cursor()

    query = """SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states
    ON states.id = cities.state_id
    ORDER BY cities.id ASC"""

    cursor.execute(query)
    for r in cursor.fetchall():
        print(r)

    cursor.close()
    db.close()
