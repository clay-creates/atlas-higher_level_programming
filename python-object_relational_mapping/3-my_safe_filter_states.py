#!/usr/bin/python3

"""
Display all values in states where name matches argument,
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
    query = """SELECT * FROM states
    WHERE BINARY name = %s
    ORDER BY states.id ASC"""

    cursor.execute(query, (state))
    for r in cursor.fetchall():
        print(r)

    cursor.close()
    db.close()
