#!/usr/bin/python3

"""
Display all cities of state specified by input,
safe from SQL injections, using MySQLdb
"""

import MySQLdb
import sys

if __name__ == "__main__":

    usr = sys.argv[1]
    pw = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(host='localhost', user=usr, passwd=pw, db=database)
    cursor = db.cursor()

    query = """SELECT cities.name
    FROM cities
    JOIN states
    ON states.id = cities.state_id
    WHERE states.name = %s
    ORDER BY cities.id ASC"""

    cursor.execute(query, (state,))
    cities = [r[0] for r in cursor.fetchall()]
    print(', '.join(cities))

    cursor.close()
    db.close()
